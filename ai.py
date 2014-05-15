#!/usr/bin/env python

import aiml
import os
import sys
import subprocess

class Chatbot():
  def __init__(self):
    self._kernel = aiml.Kernel()

  def initialize(self, aiml_dir):
    self._kernel.learn(os.sep.join([aiml_dir, '*.aiml']))
    properties_file = open(os.sep.join([aiml_dir, 'bot.properties']))
    for line in properties_file:
      parts = line.split('=')
      key = parts[0]
      value = parts[1]
      self._kernel.setBotPredicate(key, value)

  def respond(self, input):
    response = self._kernel.respond(input)
    return response

  def speak(self, response):
    cmd = "wget -q -U \"Mozilla/5.0\" -O - \"http://translate.google.com/translate_tts?tl=en-uk&q=" + response + "\" > ~/Desktop/speech.mp3"
    os.system(cmd)
    subprocess.call(["afplay", "/Users/christophersu/Desktop/speech.mp3"])

  def speakResponse(self, input):
    self.speak(self.respond(input))


def main():
  chatbot = Chatbot()
  chatbot.initialize("aiml-dir") # parameter is the aiml directory

  while True:
    n = raw_input("Input: ")
    chatbot.speakResponse(n)
    
if __name__ == '__main__':
  main()
