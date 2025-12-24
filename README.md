# folder-files-to-text
A little project just to help me turning lots of files in text, with a max size.
## Purposes:
- I use Obsidian and sometimes i want my markdown notes to be used as a context to the LLM. For this, `md2ctx.py`
- Sometimes I want to prompt an LLM and send all the code I already have as a context. So this helps me save time from copy and pasting and formatting into a LLM-friendly format. For this, `dir2ctx.py`

## Usage
Let <file> be `dir2ctx.py` or `md2ctx.py`
You use it as
```sh
  python3 <file> <directory> -o <output-file> (Optional --max-file-size <max-file-size-in-bytes>) (Optional --no-tree)
```
The `<max-file-size-in-bytes>` prevents that the have binary files being parsed.


## Ideas
- Making a tool designed `<<For Obsidian>>` That creates this kind of context-representation files by following the links. It would be a simple graph traversal with an inverted index I think.
