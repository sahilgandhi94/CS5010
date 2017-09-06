// You can import more interface and class types here.

import java.util.List;

public abstract class PS00 {

    // The examples refer to
    //
    //     foo
    //     circularModules
    //     modules1
    //     modules2
    //     list(...)
    //
    // These are public static members of the ModuleExamples class
    // defined in moduleExamples.java

    // isCircular : ListOfModule -> Boolean
    // GIVEN: a list of module descriptions
    // WHERE: no two descriptions are for the same module name
    // RETURNS: true if and only if one or more of the modules
    //     depends upon itself
    // EXAMPLES:
    //
    //     isCircular (list())  =>  false
    //
    //     isCircular (modules1)  =>  false
    //
    //     isCircular (circularModules)  =>  true

    public static boolean isCircular (List<Module> modules) {

        // Your code goes here.

    }

    // bestMode : String ListOfModule -> String
    // GIVEN: a module name M and a list of module descriptions
    // WHERE: no two descriptions are for the same module name,
    //     M is among the modules described,
    //     and none of the described modules depend upon themselves
    // RETURNS: the name of a mode (LP64, ILP64, LP32, or ILP32)
    //     that, when used to compile all of the modules that need to be
    //     compiled before module M can be used, would result in
    //     compiling the fewest modules
    // NOTE: this function may have more than one correct result
    // EXAMPLES:
    //
    //     bestMode ("Main", modules1)  =>  "LP64"
    //
    //     bestMode ("Main", modules2)  =>  "ILP32"

    public static String bestMode (String m, List<Module> modules) {

        // Your code goes here.

    }

    // bestPlan : String ListOfModule -> ListOfString
    // GIVEN: a module name M and a list of module descriptions
    // WHERE: no two descriptions are for the same module name,
    //     M is among the modules described,
    //     and none of the described modules depend upon themselves
    // RETURNS: a list of names for the modules that need to be compiled
    //     using the best mode, in the order they should be compiled,
    //     before module M can be used
    // NOTE: this function may have more than one correct result
    // EXAMPLE:
    //
    // bestPlan ("Main", modules2)  =>  list ("List", "AList", "Main")

    public static List<String> bestPlan (String m, List<Module> modules) {

        // Your code goes here.

    }

    // Your help methods go here.
}

