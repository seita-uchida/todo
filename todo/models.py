import uuid

from django.db import models


class Task(models.Model):
	class TaskType(models.TextChoices):
		MUST = "must", "Must"
		WANT = "want", "Want"

	class Status(models.TextChoices):
		PENDING = "pending", "Pending"
		DONE = "done", "Done"
		DROPPED = "dropped", "Dropped"

	title = models.CharField(max_length=255)
	type = models.CharField(max_length=10, choices=TaskType.choices)
	due_date = models.DateField(null=True, blank=True)
	execution_date = models.DateField(null=True, blank=True)
	status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
	sync_id = models.UUIDField(default=uuid.uuid4, null=True, blank=True)
	order = models.FloatField(default=0)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.title} ({self.type})"
