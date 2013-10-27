#!/usr/bin/python
# -*- coding: utf-8 -*-

# Call with a template name (in relative filepath form) as the argument

def generate(template_name):
	""" Adapted from http://jinja.pocoo.org/docs/api/#basics """
	from jinja2 import Environment, PackageLoader
	env = Environment(loader=PackageLoader('source', 'templates'))
	return env.get_template(template_name).render()

if __name__ == '__main__':
	import sys
	if len(sys.argv) > 1:
		print(generate(sys.argv[1]))
