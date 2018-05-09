from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
import random
"""
models.CharField - Used to define text with a limited number of characters. Use this to store short string information, such as a title.
models.TextField - Property for long text with no limit on the number of characters.
models.DateTimeField - Represents the date and time.
models.ForeignKey - Links to other models.
"""


class GuessNumbers(models.Model): 
    name = models.CharField(max_length = 24)
    lottos = models.CharField(max_length = 255, default = '[1, 2, 3, 4, 5, 6]')
    text = models.CharField(max_length = 255)
    num_lotto = models.IntegerField(default = 5)
    update_date = models.DateTimeField()
    def __str__(self):
        return '%s - %s' % (self.name, self.text)
    
    def generate(self):
        self.lottos = ""
        origin = list(range(1,46)) #[1, 2, 3.....44, 45]
        for _ in range(0, self.num_lotto): 
            random.shuffle(origin) 
            guess = origin[:6] 
            guess.sort()
            self.lottos += str(guess) + '\n'
        self.update_date = timezone.now()
        self.save()

    