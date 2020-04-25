# -*- coding: utf-8 -*-

"""Description"""

from docutils import nodes
from docutils.parsers.rst import directives, Directive


class Podcast(Directive):
    """Include podcast

    Usage:
    .. podcast:: TITLE
        :heading: Panel heading
    """

    required_arguments = 1
    optional_arguments = 2
    option_spec = {
        'heading': str,
        'file': str,
    }
    final_argument_whitespace = False
    has_content = False

    def run(self):
        heading = self.options.get('heading', u'')
        title = self.arguments[0].strip()
        file_ = self.options.get('file', title)

        html = u"""
        <div class="podcast text-center">
            <iframe src="https://archive.org/embed/{title}" width="80%" height="30" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe>

            <div class="podcast-download">
                <a class="btn btn-primary btn-sm" href="https://archive.org/download/{title}/{file}.mp3"><i class="fa fa-download"></i> MP3</a>
                <a class="btn btn-primary btn-sm" href="https://archive.org/download/{title}/{file}.ogg"><i class="fa fa-download"></i> OGG</a>
            </div>
        </div>
        """.format(title=title, file=file_)

        if heading:
            html = u"""
            <div class="panel panel-default">
                <div class="panel-heading">{0}</div>
                <div class="panel-body">
                    {1}
                </div>
            </div>
            """.format(heading, html)

        return [nodes.raw('', html, format='html')]


def register():
    directives.register_directive('podcast', Podcast)
