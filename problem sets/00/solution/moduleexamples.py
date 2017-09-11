

from modules import Modules
from PS00 import PS00


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

    modules3 = [Modules.makeModule("Main", ["List", "AList"], 0, 11, "LP64"),
                Modules.makeModule(
                    "List", ["Obj"], 0, 11, "LP64"),
                Modules.makeModule(
                    "AList", ["List", "Obj"], 0, 11, "LP64"),
                Modules.makeModule("Obj", [], 0, 11, "LP64")]

    modules4 = [Modules.makeModule("Main", ["List", "AList"], 3, 10, "ILP32"),
                Modules.makeModule("List", ["Obj"], 1, 4, "ILP64"),
                Modules.makeModule("AList", ["A1", "A2"], 5, 4, "ILP32"),
                Modules.makeModule("Obj", ["O1", "O2"], 1, 2, "LP32"),
                Modules.makeModule("O1", [], 1, 3, "LP32"),
                Modules.makeModule("O2", ["A3"], 1, 4, "LP32"),
                Modules.makeModule("A1", [], 1, 2, "LP64"),
                Modules.makeModule("A2", ["A3"], 1, 2, "LP64"),
                Modules.makeModule("A3", [], 2, -1, "LP64")]


if __name__ == '__main__':
    soln = PS00()
    print('Circular Test for circularmodules ===>', soln.isCircular(ModuleExamples.circularModules))
    print('Circular Test for modules1 ===>', soln.isCircular(ModuleExamples.modules1))
    print('Circular Test for modules2 ===>', soln.isCircular(ModuleExamples.modules2))
    print('Circular Test for modules3 ===>', soln.isCircular(ModuleExamples.modules3))
    print('Circular Test for modules4 ===>', soln.isCircular(ModuleExamples.modules4))
    print('BestMode Test for modules1 ===>', soln.bestMode('Main', ModuleExamples.modules1))
    print('BestMode Test for modules2 ===>', soln.bestMode('Main', ModuleExamples.modules2))
    print('BestMode Test for modules3 ===>', soln.bestMode('Main', ModuleExamples.modules3))
    print('BestMode Test for modules4 ===>', soln.bestMode('Main', ModuleExamples.modules4))
    print('BestPlan Test for modules1 ===>', soln.bestPlan('Main', ModuleExamples.modules1))
    print('BestPlan Test for modules2 ===>', soln.bestPlan('Main', ModuleExamples.modules2))
    print('BestPlan Test for modules3 ===>', soln.bestPlan('Main', ModuleExamples.modules3))
    print('BestPlan Test for modules4 ===>', soln.bestPlan('Main', ModuleExamples.modules4))
    print('============= FIN =============')
