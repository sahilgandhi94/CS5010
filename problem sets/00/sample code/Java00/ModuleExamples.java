// Examples for Problem Set 00.
//
// Students should write their own examples for complete glass-box
// testing of their implementations.
//
// The examples used for grading will not be exactly the same as
// these examples.

import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;


/**
 * Defines some examples for testing and makes them available as
 * public members of the class.
 */

public class ModuleExamples {

    // abbreviation

    private static Module makeModule (String name,
                                      List<String> uses,
                                      int mtime,
                                      int ctime,
                                      String cmode) {
        return Modules.makeModule (name, uses, mtime, ctime, cmode);
    }

    // a description of a module that's been modified since it was compiled
    // and must therefore be compiled again before it is used

    public static Module foo
        = makeModule ("Foo", list ("Baz"), 1505109465, 1504097449, "LP64");

    // a list of modules that have a circular dependency

    public static List<Module> circularModules
        = list (makeModule ("M1", list ("M2", "M3"), 1500, -1, "ILP32"),
                makeModule ("M2", list ("M3"),       2000, -1, "ILP32"),
                makeModule ("M3", list ("M2"),       2500, -1, "ILP32"));

    // a list of modules, of which only Main needs to be compiled
    // (in mode LP64) before Main can be used

    public static List<Module> modules1
        = list (makeModule ("Main",
                            list ("List", "AList"),
                            1504188920,
                            -1,
                            "LP64"),
                makeModule ("List",
                            list ("Obj"),
                            1472652920,
                            1472658760,
                            "LP64"),
                makeModule ("AList",
                            list ("List", "Obj"),
                            1472654764,
                            1472659242,
                            "LP64"),
                makeModule ("Obj",
                            list(),
                            1472630256,
                            1472638841,
                            "LP64"));

    // a list of modules, of which List, AList, and Main need to be compiled
    // (in that order, in mode ILP32) before Main can be used

    public static List<Module> modules2
        = list (makeModule ("Main",
                            list ("List", "AList"),
                            1504188920,
                            -1,
                            "LP64"),
                makeModule ("List",
                            list ("Obj"),
                            1472652920,
                            1472658760,
                            "LP64"),
                makeModule ("AList",
                            list ("List", "Obj"),
                            1472654764,
                            1472659242,
                            "LP64"),
                makeModule ("Obj",
                            list(),
                            1472630256,
                            1472638841,
                            "ILP32"));

    // more abbreviations

    public static List<String> list () {
        List<String> result = new ArrayList<String>();
        return result;
    }

    public static List<String> list (String s1) {
        List<String> result = new LinkedList<String>();
        result.add (s1);
        return result;
    }

    public static List<String> list (String s1, String s2) {
        List<String> result = new ArrayList<String>();
        result.add (s1);
        result.add (s2);
        return result;
    }

    public static List<String> list (String s1, String s2, String s3) {
        List<String> result = new LinkedList<String>();
        result.add (s1);
        result.add (s2);
        result.add (s3);
        return result;
    }

    public static List<String> list (String s1,
                                     String s2,
                                     String s3,
                                     String s4) {
        List<String> result = new ArrayList<String>();
        result.add (s1);
        result.add (s2);
        result.add (s3);
        result.add (s4);
        return result;
    }

    public static List<Module> list (Module m1) {
        List<Module> result = new ArrayList<Module>();
        result.add (m1);
        return result;
    }

    public static List<Module> list (Module m1, Module m2) {
        List<Module> result = new LinkedList<Module>();
        result.add (m1);
        result.add (m2);
        return result;
    }

    public static List<Module> list (Module m1, Module m2, Module m3) {
        List<Module> result = new ArrayList<Module>();
        result.add (m1);
        result.add (m2);
        result.add (m3);
        return result;
    }

    public static List<Module> list (Module m1,
                                     Module m2,
                                     Module m3,
                                     Module m4) {
        List<Module> result = new LinkedList<Module>();
        result.add (m1);
        result.add (m2);
        result.add (m3);
        result.add (m4);
        return result;
    }
}
