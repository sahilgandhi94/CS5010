

from modules import Modules
from graph import Graph


class ModuleExamples:

    # def _makeModule(self, name, uses, mtime, ctime, cmode):
    #     return Modules.makeModule(name, uses, mtime, ctime, cmode)

    # a description of a module that's been modified since it was compiled
    # and must therefore be compiled again before it is used
    foo = Modules.makeModule("Foo", ["Baz"], 1505109465, 1504097449, "LP64")

    # a list of modules that have a circular dependency
    circularModules = [Modules.makeModule("M1", ["M2", "M3"], 1500, -1, "ILP32"),
                       Modules.makeModule("M2", ["M3"], 2000, -1, "ILP32"),
                       Modules.makeModule("M3", ["M2"], 2500, -1, "ILP32")]

    # a list of modules, of which only Main needs to be compiled
    # (in mode LP64) before Main can be used
    modules1 = [Modules.makeModule("Main", ["List", "AList"], 1504188920, -1, "LP64"),
                Modules.makeModule(
                    "List", ["Obj"], 1472652920, 1472658760, "LP64"),
                Modules.makeModule(
                    "AList", ["List", "Obj"], 1472654764, 1472659242, "LP64"),
                Modules.makeModule("Obj", [], 1472630256, 1472638841, "LP64")]

    # a list of modules, of which List, AList, and Main need to be compiled
    # (in that order, in mode ILP32) before Main can be used
    modules2 = [Modules.makeModule("Main", ["List", "AList"], 1504188920, -1, "LP64"),
                Modules.makeModule(
                    "List", ["Obj"], 1472652920, 1472658760, "LP64"),
                Modules.makeModule(
                    "AList", ["List", "Obj"], 1472654764, 1472659242, "LP64"),
                Modules.makeModule("Obj", [], 1472630256, 1472638841, "ILP32")]


if __name__ == '__main__':
    print(Graph.makegraph(ModuleExamples.modules1))
