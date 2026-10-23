import argparse
import json
import sqlite3
import sys
from pathlib import Path

from .core import Workflow, scenario
from .evaluation import evaluate
from .labs import write_lab


def main():
    parser = argparse.ArgumentParser(description="Offline AI engineering lab")
    parser.add_argument("--db", default=".runs/support.db")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("demo")
    commands.add_parser("report")
    commands.add_parser("eval")
    draft = commands.add_parser("draft")
    draft.add_argument("ticket", choices=[t["id"] for t in scenario()["tickets"]])
    inspect = commands.add_parser("inspect")
    inspect.add_argument("ticket")
    for name in ["approve", "reject"]:
        decision = commands.add_parser(name)
        decision.add_argument("ticket")
        decision.add_argument("--actor", required=True, choices=["alice", "bob"])
        decision.add_argument("--digest", required=True, help="Digest of the exact inspected action")
    send = commands.add_parser("send")
    send.add_argument("ticket")
    lab = commands.add_parser("lab")
    lab.add_argument("number", help="1–13 or all")
    lab.add_argument("--out", type=Path, default=Path(".runs/labs"))
    args = parser.parse_args()
    try:
        if args.command == "lab":
            numbers = range(1, 14) if args.number == "all" else [int(args.number)]
            for number in numbers:
                print(write_lab(number, args.out))
            return 0
        if args.command == "eval":
            result = evaluate()
            print(json.dumps(result, indent=2))
            return 0 if result["quality_pass_rate"] == 1 and result["recall_at_2"] == 1 else 1
        path = Path(args.db)
        path.parent.mkdir(parents=True, exist_ok=True)
        app = Workflow(path)
        try:
            if args.command in {"draft", "demo"}:
                tickets = scenario()["tickets"]
                if args.command == "draft":
                    tickets = [t for t in tickets if t["id"] == args.ticket]
                result = [app.draft(t) for t in tickets]
            elif args.command == "inspect":
                result = app.inspect(args.ticket)
            elif args.command in {"approve", "reject"}:
                app.decide(args.ticket, args.actor, args.digest, approve=args.command == "approve")
                result = app.inspect(args.ticket)
            elif args.command == "send":
                result = app.send(args.ticket)
            else:
                result = app.report()
            print(json.dumps(result, indent=2))
        finally:
            app.close()
        return 0
    except (ValueError, PermissionError, AssertionError, sqlite3.Error) as error:
        print(f"Refused: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
