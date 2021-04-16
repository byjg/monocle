# Monocle.
# Copyright (C) 2019-2021 Monocle authors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from typing import List, Optional, Dict
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class TaskData:
    crawler_name: str
    updated_at: datetime
    change_url: str
    issue_type: List[str]
    issue_id: str
    issue_url: str
    issue_title: str
    severity: Optional[str] = None
    priority: Optional[str] = None
    score: Optional[int] = None


InputTaskData = List[TaskData]


@dataclass
class TaskCrawler:
    name: str
    api_key: str
    updated_since: datetime


def createInputTaskData(data: List, crawler_name: str) -> InputTaskData:
    def createTaskData(td: Dict) -> TaskData:
        # TODO(fbo): we probably need more validation here
        if not isinstance(td["issue_type"], list):
            raise ValueError("issue_type must be a list")
        return TaskData(
            crawler_name=crawler_name,
            updated_at=datetime.strptime(td["updated_at"], "%Y-%m-%dT%H:%M:%SZ"),
            change_url=td["change_url"],
            issue_type=td["issue_type"],
            issue_id=td["issue_id"],
            issue_url=td["issue_url"],
            issue_title=td["issue_title"],
            severity=td.get("severity"),
            priority=td.get("priority"),
            score=td.get("score"),
        )

    return [createTaskData(td) for td in data]


def createELTaskData(data: List) -> InputTaskData:
    def createTaskData(td: Dict) -> TaskData:
        return TaskData(
            crawler_name=td["crawler_name"],
            updated_at=td["updated_at"],
            change_url=td["change_url"],
            issue_type=td["issue_type"],
            issue_id=td["issue_id"],
            issue_url=td["issue_url"],
            issue_title=td["issue_title"],
            severity=td.get("severity"),
            priority=td.get("priority"),
            score=td.get("score"),
        )

    return [createTaskData(td) for td in data]


def createTaskCrawler(raw: Dict) -> TaskCrawler:
    return TaskCrawler(
        name=raw["name"],
        api_key=raw["api_key"],
        updated_since=datetime.strptime(raw["updated_since"], "%Y-%m-%d"),
    )


@dataclass
class TaskDataForEL:
    _id: str
    tracker_data: InputTaskData


@dataclass
class OrphanTaskDataForEL:
    _id: str
    tracker_data: TaskData


@dataclass
class AdoptedTaskData:
    _adopted: bool


@dataclass
class AdoptedTaskDataForEL:
    _id: str
    tracker_data: AdoptedTaskData
