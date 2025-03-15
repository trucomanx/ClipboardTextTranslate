# clipboard-text-translate

Program that translate text

## Testar indicator

```bash
cd src
python3 -m clipboard_text_translate.indicator
```

## Upload to PYPI

```bash
cd src
python setup.py sdist bdist_wheel
twine upload dist/*
```

## Install from PYPI

The homepage in pipy is https://pypi.org/project/clipboard-text-translate/

```bash
pip install --upgrade clipboard-text-translate
```

Using:

```bash
clipboard-text-translate-indicator
```

## Install from source
Installing `clipboard-text-translate` program

```bash
git clone https://github.com/trucomanx/ClipboardTextTranslate.git
cd ClipboardTextTranslate
pip install -r requirements.txt
cd src
python3 setup.py sdist
pip install dist/clipboard_text_translate-*.tar.gz
```
Using:

```bash
clipboard-text-translate-indicator
```

## Uninstall

```bash
pip uninstall clipboard_text_translate
```
