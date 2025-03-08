from datetime import datetime, date
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    email: str

user = User("daisuke", "daisuke@example.com")
print(user.name)
print(user.email)

# デフォルト値
@dataclass
class User_sample:
    name: str
    age: int
    birthday: date
    phonenuber: str = ""
    is_admin: bool = False
    last_login: datetime = datetime.now()

# デフォルト値_空リスト
@dataclass
class User_Sample_List:
    name: str
    item: list[str] = field(default_factory=list)

# デフォルト値_リスト
@dataclass
class User_Sample_Apple_List:
    name: str
    item: list[str] = field(default_factory=lambda: ["Apple"])

