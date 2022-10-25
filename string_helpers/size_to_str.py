#
# Function to convert bytes into MB, GB, etc.
#

@overload
def size_to_str(size_bytes: int) -> str:
    """Converts number of bytes to a human readable string using SI units."""
    ...
    
@overload
def size_to_str(size_bytes: float) -> str:
    """Converts number of bytes to a human readable string using SI units."""
    ...
    
@overload
def size_to_str(size_bytes: object) -> str:
    """
    Checks the size of an object before returning the human readable size in SI units.
    """
    ...
    
def size_to_str(size_bytes) -> str:
    """
    Converts number of bytes to a human readable string using SI units. If passed an object, first checks the size
    before returning the human readable string representing the size in SI units.
    """

    if isinstance(size_bytes, float):
        logger.warning("`size_bytes` is a float. Treating as an integer.")
        size_bytes = int(size_bytes)

    if not isinstance(size_bytes, int):
        size_bytes = sys.getsizeof(size_bytes)

    if size_bytes == 0:
        return "0B"
        
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

logger.debug(size_to_str(11.1))
