// To make this sample implementation as simple as possible,
// everything goes into the default package.

import java.util.List;

/**
 * Represents information describing one module of a program.
 */

public interface Module {

    /**
     * @return         the name of this module
     */

    public String moduleName();

    /**
     * @return         the names of modules used by this module
     */

    public List<String> moduleUses();

    /**
     * @return         the time (in seconds since 1 January 1970)
     *                 when this module's source code was last modified
     */

    public int modificationTime();

    /**
     * @return         the time (in seconds since 1 January 1970)
     *                 when this module was last compiled, or -1
     *                 if it hasn't been compiled
     */

    public int compilationTime();

    /**
     * @return         the mode ("LP64", "ILP64", "ILP32", or "LP32")
     *                 in which this module was last compiled; the
     *                 result is meaningless if it hasn't been compiled
     */

    public String compilationMode();

}
