

from abc import ABCMeta

from module import Module


class Modules(metaclass=ABCMeta):

    @staticmethod
    def makeModule(name, uses, mtime, ctime, cmode):
        return _Module0(name, uses, mtime, ctime, cmode)


class _Module0(Module):

    def __init__(self, name, uses, mtime, ctime, cmode):
        self._name = name
        self._uses = uses
        self._mtime = mtime
        self._ctime = ctime
        self._cmode = cmode
    
    @property
    def moduleName(self):
        return self._name

    @property
    def moduleUses(self):
        return self._uses

    @property
    def modificationTime(self):
        return self._mtime

    @property
    def compilationTime(self):
        return self._ctime

    @property
    def compilationMode(self):
        return self._cmode

    def equals(self, mod):
        if not mod:
            return False
        elif not isinstance(mod, Module):
            return False
        else:
            return self.sameModule(mod)

    def sameModule(self, mod):
        if (
            self.moduleName == mod.moduleName and
            self.moduleUses == mod.moduleUses and
            self.modificationTime == mod.modificationTime and 
            self.compilationTime == mod.compilationTime and
            self.compilationMode == -1
        ):
            return True
        else:
            return self.compilationMode == mod.compilationMode

    def __repr__(self):
        final = '{}: uses('.format(self.moduleName)
        for string in self.moduleUses:
            final += ' {},'.format(string)
        final = final[0: len(final)-1]
        final += '){}:{}:{}'.format(self.modificationTime, self.compilationTime, self.compilationMode)

    def __hash__(self):
        return hash(self.__repr__())
