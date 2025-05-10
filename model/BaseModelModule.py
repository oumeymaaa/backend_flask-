import datetime
from typing import Optional

from pydantic import BaseModel

class BaseModelApp(BaseModel):
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None

    def timestamp_snapshot(self):
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
