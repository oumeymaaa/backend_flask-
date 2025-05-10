import datetime
from pydantic import BaseModel
from typing import Optional

from database.NotificationCollection import NotificationCollection

class NotificationModel(BaseModel):
    user_id: str
    category: str
    title: str
    body: str
    data: dict
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None

    def timestamp_snapshot(self):
        """Met à jour les timestamps de création et de mise à jour"""
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def dict(self):
        """Retourne un dictionnaire des données du modèle"""
        data = super().dict()
        data[NotificationCollection.CREATED_AT] = self.created_at
        data[NotificationCollection.UPDATED_AT] = self.updated_at
        return data
