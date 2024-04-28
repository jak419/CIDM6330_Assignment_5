import csv
from pathlib import Path
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Bookmark

# Initialize channel layer
channel_layer = get_channel_layer()

@receiver(post_save, sender=Bookmark)
def log_bookmark_to_csv(sender, instance, created, **kwargs):
    print("Logging Bookmark to CSV")

    file_path = Path(__file__).resolve().parent / "logs" / "created_log.csv"
    print(f"Writing to {file_path}")

    with open(file_path, "a+", newline="") as csvfile:
        logwriter = csv.writer(csvfile, delimiter=',')
        logwriter.writerow([instance.id, instance.title, instance.url, instance.notes, instance.date_added])

@receiver(post_save, sender=Bookmark)
def send_bookmark_to_channel(sender, instance, created, **kwargs):
    print("Sending Bookmark to Channel")
    group_name = "bookmarks_group"

    # Send to WebSocket
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            "type": "bookmark_update",
            "message": {
                "id": instance.id,
                "title": instance.title,
                "url": instance.url,
                "notes": instance.notes,
                "date_added": str(instance.date_added)
            }
        }
    )

@receiver(post_save, sender=Bookmark)
def log_bookmark_activity(sender, instance, created, **kwargs):
    action = "created" if created else "updated"
    print(f"Bookmark {action}: {instance.title}")

@receiver(post_delete, sender=Bookmark)
def log_bookmark_deletion(sender, instance, **kwargs):
    print(f"Bookmark deleted: {instance.title}")
