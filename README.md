# Colinote

Colinote is a command-line tool for managing notes.

## Installation

You can install Colinote using pip:

```
pip install colinote
```


## Usage

To use Colinote, simply run the colinote command followed by the action you want to perform and any relevant options.

## Actions
*add:* Add a new note to a context.

*edit:* Edit an existing note.

*delete:* Delete an existing note.

*show*: List all notes or all notes for a specific id,context or date.

*Options*
- *-c, --context:* The context for the note.
- *-t, --text:* The text of the note.
- *-d, --date:* The date of the note (in the format "YYYY-MM-DD").
- *-i, --id:* The ID of the note.

### Examples

*Add a note in default context (todo)*
```
colinote add "I did something amazing"
```

*Add a note in context "standup"*
```
colinote add "I did something amazing" -c "standup"
```

*Edit a note with id 1 and change the text*
```
colinote edit 1 -t "I did something even more amazing"
```

*Edit a note with id 1 and change the context*
```
colinote edit 1 -c "standup"
```

*Delete note with id 1*
```
colinote delete 1
```

*List all notes*
```
colinote show
```

*List all notes for a specific context*
```
colinote show -c "work"
```

*List all notes for a specific date*
```
colinote show -d "2023-01-01"
```

*Show a specific note*
```
colinote show -i 1
```

## Contributing
Contributions are always welcome! Here are some ways to contribute:

- Fork the repository and make changes on your local branch.
- Create a pull request with your changes.
- Work on open issues.

## Development

To develop Colinote, first clone the repository:
```
git clone https://github.com/tiakas/colinote.git`
cd colinote
```
Then, install the development dependencies:

```
pip install -r requirements.txt
```

To run the tests, use:
```
pytest
```

To build the package, use:
```
python setup.py sdist bdist_wheel
```

This will create a dist directory containing the source distribution (*.tar.gz) and wheel distribution (*.whl) of the package.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
