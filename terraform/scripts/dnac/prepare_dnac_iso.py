import json
import base64
import zlib
#import file_utils

MAGLEV_CONFIG_SIZE = 8196
MAGLEV_CDROM_HEADER = """
H4sIAP/9IFgCA+3bTUvcQBjA8UQsigUvUtTSw1A8tBTXRGVl6Smdnd0dTTJhJit6kiIqLb5Atb17
agv9OD33s/gFpB+hzewLrdpWCqUW+/+xuzPJPHlmQgJDwk4QAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAUDajKA6DVOfdDfFzB8/39nfezG8fHe6+2PtB+zDf
xwvFL/qtPv4bjI8HE/1dE1Pfmu/5n4fBdH9rOhj3xXhwcndscurJ2cjweIEb1Va5dkZnSVuJqiIa
9Xq00Gk50dKpcpuuVJmQViWlseKRfCziRmNJqNqm6ebtZpKq4c6V+cUoqovVWqES60y+sFpzsqPT
6q5s92J8s49ZEbJp13QpSpVkf/10F6O4HsfRSrwcN5aXoujsyo7okuBKBDft/45JB/+ML4P5HwAA
AAAA3F5h7x07z/8AAAAAANzu5//A/7+OFwAAAAAAANxi765dY+eKsfDT58DaO+FpsTEXHiQ+LjkY
6R83cjlj2bofTg6SXCykehDO9INmhtHng2L3unGEf2AAwYdgth8zOyp8IUaHLf1eJmXadaWyW7VV
Z57GvZN+n2czYbC9//r4ZOfVYAFk7eXx0aEfy9ypT3M6N3h/Ev7GWAAAuDnKnocT5dtqdtXFVtxo
xEnZUcIauSasbvpl3Xk1H8pOklf1wprSSJP6yrpuKidctyiMLUXLWFEYpzd6K7/FYOm3U1mSl1q6
IlWJU0KavExkKZraSVF0n6XadZTtHewKJXVLy6TUJhfOdK1UNVFlUN8FVl1W6VraV/NqEDpL7KZY
N2k3U6IajqxOwi819wmHfem82sp6aWtcbgAAer4CnVlwtwDIAAA="""

MAGLEV_CDROM_FOOTER = """
H4sIAP/9IFgCA+3BMQEAAADCoPVPbQ0PoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4NsACMdiV/y3BAA="""

def write_file(path, content, write_type=""):
    """ This method writes to a file.

    Args:
        path (str): path of the file to read
        content (str): content to write in the file
        write_type (str): type to open the file

    Returns:
        boolean: depending on the success/failure of the task

    Raises:
        Exception: if writing in the file fails.
    """

    if write_type and write_type != "b":
        raise Exception("Invalid write type: {}".format(write_type))
    try:
        with open(path, 'w'+write_type) as f:
            return f.write(content)
    except:
        raise Exception("Failed to write file - {}".format(path))

def maglev_cdrom(os_conf):
    """ Generates content of Maglev Config cdrom containing the configuration 'maglev_conf'

    Args:
        os_conf (str): path to controller-config.json

    Returns:
        bytes: Content of the floppy
    """
    def decode(data):

        decoded_content = base64.decodebytes(data.encode())
        return zlib.decompress(decoded_content, 16+zlib.MAX_WBITS)

    def pad(data, length):

        return data + '\n' * (length - len(data))

    return (decode(MAGLEV_CDROM_HEADER) +
            pad(os_conf, MAGLEV_CONFIG_SIZE).encode() +
            decode(MAGLEV_CDROM_FOOTER))

with open("controller_config.json", 'r') as file:
        data = json.load(file)
cdrom_config = json.dumps(data).replace("\n", "").replace(" ", "")
maglev_conf = maglev_cdrom(cdrom_config)

write_file("dnac-config-cdrom.iso", maglev_conf, write_type="b")