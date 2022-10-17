# About ipaFram

**ipaFram** was written in order to help any mobile penetration testers to identify the Framework used to develop the iOS application.

## Usage

Print the help to get all necessary information

```bash
$ python3 ipaFram.py -h
usage: ipaFram.py [-h] [--file FILE]

iOS Framework Identifier

optional arguments:
  -h, --help   show this help message and exit
  --file FILE  Specify your IPA file
```

You just have to specify the IPA file in input to get the used framework:

```bash
$ python3 ipaFram.py --file examples/dvia.ipa
[!] No framework detected

$ python3 ipaFram.py --file examples/xam.ipa
[!] Xamarin seems to be the best probability
```

Currently supported frameworks:

* ReactNative
* ReactNative compiled with Hermes


## Author

Régis SENET ([rsenet](https://github.com/rsenet))


## Contributing

Bug reports and pull requests are welcome on [GitHub](https://github.com/rsenet/ipaFram).

## License

The project is available as open source under the terms of the [GPLv3](https://www.gnu.org/licenses/quick-guide-gplv3.en.html)
