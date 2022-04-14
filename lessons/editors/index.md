![Ivy logo](https://raw.githubusercontent.com/csdms/ivy/main/media/logo.png)

# Text Editors and Development Environments

In this short lesson
we'll learn about *text editors* and *development environments*,
programs that help you write code.

*Learning objectives:*

* Understand the difference between a text editor and a word processor
* Know when to use a text editor
* See common traits of text editors
* Understand what a development environment is

## Rich text, plain text

What is plain text and what is rich text?
Broadly:

* *Plain text* is made from the characters you see on your keyboard.
Plain text is stored in a text file.
Code is plain text.
This Markdown file is plain text.

* *Rich text* is formed from plain text,
but includes additional metadata
like fonts, styles, colors, and other formatting.
Rich text may include embedded images and videos.
Rich text is typically stored in a binary, often proprietary, file format.
A Microsoft Word doc is rich text.

*Text editors* are designed to work with plain text.
*Word processors* are designed to work with rich text.
It's difficult (but not impossible)
to create one type of text with the tool designed for the other,
but just as a screwdriver can sometimes be used as a hammer,
it's not necessarily the best idea.

## Text editors

Text editors help you write code.
For example, most offer features such as
* syntax highlighting
* command completion
* automatic indentation
* parenthesis and bracket matching

Free and open source
text editors that are typically installed on a UNIX-based operating system include
[nano][nano],
[vi/m][vim], and
[emacs][emacs].
A sampling of other prominent text editors (some of which you have to pay for) includes
[VS Code][code],
[Sublime Text][sublime],
[Atom][atom],
[TextMate][textmate] (macOS),
[Nova][nova] (macOS), and
[Notepad++][nppp] (Windows).

Every text editor has its advantages and disadvantages.
It's best to find one you like and learn how to use it well.

## Development environments

An *integrated development environment* (IDE)
is a program that includes a comprehensive set of tools for creating software.
IDEs amalgamate tools of the software development process that are typically distributed across text editors, shell programs, and websites.
The distinction between a text editor and an IDE is heavily blurred, though;
typically, we can consider an IDE to contain a text editor
as one of its components.

Two popular IDEs for Python are
[Spyder][spyder] and
[PyCharm][pycharm].

The choice between using an IDE versus a text editor plus other tools is largely a matter of taste.

## Summary

Code is text.
Write code with a text editor.
It doesn't really matter which text editor you use--find one you like
and learn how to use it well.
Don't write code with a word processor.
Plain text is [future-proof](https://en.wikipedia.org/wiki/Future-proof).

This table summarizes the concepts covered in this lesson:

| Concept      | Description
| ------------ | -----------
| plain text | Text without formatting
| rich text | Text with formatting
| text editor | A program for writing plain text
| word processor | A program for writing rich text
| integrated development environment | A program with a comprehensive set of tools for creating software

***Note #1***

We don't use text editors often in Ivy
because most of the course material is in Jupyter Notebook.
However,
when you write code for school or work,
you will undoubtedly use a text editor (or an IDE).

***Note #2***

Don't get so attached to your text editor that you think your choice is superior to others.
[Seriously][editor-war].

## Resources

* [Plain text vs. rich text](https://en.wikipedia.org/wiki/Text_editor#Plain_text_vs._rich_text)
* [A list of text editors](https://en.wikipedia.org/wiki/List_of_text_editors)

<!-- Links (by alpha) -->

[atom]: https://en.wikipedia.org/wiki/Atom_(text_editor)
[code]: https://en.wikipedia.org/wiki/Visual_Studio_Code
[editor-war]: https://en.wikipedia.org/wiki/Editor_war
[emacs]: https://en.wikipedia.org/wiki/Emacs
[nano]: https://en.wikipedia.org/wiki/GNU_nano
[nova]: https://nova.app/
[nppp]: https://en.wikipedia.org/wiki/Notepad%2B%2B
[pycharm]: https://en.wikipedia.org/wiki/PyCharm
[spyder]: https://en.wikipedia.org/wiki/Spyder_(software)
[sublime]: https://en.wikipedia.org/wiki/Sublime_Text
[textmate]: https://en.wikipedia.org/wiki/TextMate
[vim]: https://en.wikipedia.org/wiki/Vim_(text_editor)
