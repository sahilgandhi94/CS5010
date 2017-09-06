// To make this sample implementation as simple as possible,
// everything goes into the default package.

import java.util.List;

/**
 * Implements a static factory method for creating Module objects.
 */

public abstract class Modules {

    /**
     * Static factory method for creating descriptions of modules.
     *
     * @param name     the name of the module
     * @param uses     the list of names for modules it uses
     * @param mtime    time when source code was last modified
     * @param ctime    time when last compiled, or -1 if not compiled
     * @param cmode    mode in which the module was last compiled
     * @return         a Module object that encapsulates the given information
     */

    public static Module makeModule (String name, List<String> uses,
                                     int mtime, int ctime, String cmode) {
         return new Module0 (name, uses, mtime, ctime, cmode);
    }

    private static class Module0 implements Module {

        private String name;       // name of this module
        private List<String> uses; // names of modules this module uses
        private int mtime;         // source code modification time
        private int ctime;         // time of last compilation or -1
        private String cmode;      // mode of last compilation

        Module0 (String name, List<String> uses,
                 int mtime, int ctime, String cmode) {
            this.name = name;
            this.uses = uses;
            this.mtime = mtime;
            this.ctime = ctime;
            this.cmode = cmode;
        }

        /**
         * @return         {@inheritDoc}
         */

        public String moduleName() { return name; }

        /**
         * @return         {@inheritDoc}
         */

        public List<String> moduleUses() { return uses; }

        /**
         * @return         {@inheritDoc}
         */

        public int modificationTime() { return mtime; }

        /**
         * @return         {@inheritDoc}
         */

        public int compilationTime() { return ctime; }

        /**
         * @return         {@inheritDoc}
         */

        public String compilationMode() { return cmode; }

        /**
         * {@inheritdoc}
         */

        public boolean equals (Object x) {
            if (x == null)
                return false;
            else if (! (x instanceof Module))
                return false;
            else
                return sameModule ((Module) x);
        }

        private boolean sameModule (Module m) {
            return name.equals (m.moduleName()) &&
                uses.equals (m.moduleUses()) &&
                (mtime == m.modificationTime()) &&
                (ctime == m.compilationTime()) &&
                ((ctime == -1) ? true : (cmode.equals (m.compilationMode())));
        }

        /**
         * {@inheritdoc}
         */

        public String toString() {
            String s = name + ":uses(";
            for (String s2 : uses)
                s = s + s2 + ",";
            s = s.substring (0, s.length() - 1); // FIXME: assumes BMP
            s = s + ")" + mtime + ":" + ctime + ":" + cmode;
            return s;
        }

        /**
         * {@inheritdoc}
         */

        public int hashCode() {
            return toString().hashCode();
        }
    }
}
