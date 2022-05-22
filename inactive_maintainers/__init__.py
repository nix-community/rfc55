import os
import sys
from datetime import date, datetime, time
from sys import stderr

from github import Github
from github.Commit import Commit
from github.PaginatedList import PaginatedList


def has_commits(commits: "PaginatedList[Commit]") -> bool:
    # totalCount is borked, len(list(...)) eats too many API calls
    try:
        commits[0]
        return True
    except IndexError:
        return False


def main() -> None:
    token = os.environ.get("GITHUB_TOKEN", None)
    if token is None:
        print("environment variable GITHUB_TOKEN not set", file=sys.stderr)
        sys.exit(1)
    year = date.today().year - 1
    start_of_year = datetime.combine(date(year, 1, 1), time.min)
    print(f"Reporting from {start_of_year}")
    gh = Github(
        os.environ["GITHUB_TOKEN"],
        user_agent="nixpkgs-inactive-committers",
        per_page=100,
        timeout=90,
        retry=5,
    )
    print(gh.get_rate_limit(), file=stderr)
    org = gh.get_organization("nixos")
    nixpkgs = org.get_repo("nixpkgs")
    committers = org.get_team_by_slug("nixpkgs-committers").get_members()
    sorted_committers = sorted(list(committers), key=lambda c: c.login.lower())

    blacklist = ["GrahamcOfBorg"]

    for member in sorted_committers:
        if member in blacklist:
            continue
        commits = nixpkgs.get_commits(author=member, since=start_of_year)
        if not has_commits(commits):
            print(
                f"- @{member.login:<20} [commits](https://github.com/NixOS/nixpkgs/commits?author={member.login})"
            )


if __name__ == "main":
    main()
