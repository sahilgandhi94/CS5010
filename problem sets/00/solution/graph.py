

from collections import defaultdict


class Graph:
    ''' graph implementation to denote the hierarchy of the modules and its dependencies '''

    def __init__(self):
        # initialize an empty adjancy matrix
        self.adj = defaultdict(list)  # dictionary structure: {module object: list of modules, ...}

    def __repr__(self):
        # return json.dumps(self.adj, indent=4)
        final = ''
        for mod, uses in self.adj.items():
            final += '{} --> {}\n'.format(mod.moduleName, [module.moduleName for module in uses])
        return final

    def addedge(self, source, destination):
        ''' add an edge, originating from u and ending at v '''
        self.adj[source].append(destination)

    def order(self, module=None):
        ''' returns the depth first traversal of the graph
            if a module (or it's description) is provided then the dfs traversal begins from that node
            if the provided module is not found or not provided at all, then a random node is selected
        '''
        visited = {module: False for module in self.adj.keys()}
        order = list()  # dfs traversal order to be returned

        if module:
            if isinstance(module, str):
                module = self._getmodule(module)
            if not self._isvisited(module, visited):
                self._dfsorder(module, visited, order)
        else:
            for module in self.adj.keys():
                if not self._isvisited(module, visited):
                    self._dfsorder(module, visited, order)
        return order

    def _dfsorder(self, module, visited, order):
        visited[module] = True
        for mod in self.adj[module]:
            # traverse the adjancy list of the node
            if not self._isvisited(mod, visited):
                self._dfsorder(mod, visited, order)
        order.append(module)

    def iscyclic(self):
        ''' returns true if the graph contains cyclic groups '''
        visited = {module: False for module in self.adj.keys()}
        cyclic = {module: False for module in self.adj.keys()}

        for module in self.adj.keys():
            if not self._isvisited(module, visited):
                if self._checkcyclic(module, visited, cyclic):
                    return True
        return False

    def _checkcyclic(self, module, visited, cyclic):
        visited[module] = True
        cyclic[module] = True
        for mod in self.adj[module]:
            if not self._isvisited(mod, visited):
                if self._checkcyclic(mod, visited, cyclic):
                    return True
            elif cyclic[mod]:
                return True
        cyclic[module] = False
        return False

    def _isvisited(self, module, visited):
        return visited[module]

    def _getmodule(self, desc):
        ''' returns the module object based on the given description '''
        for module in self.adj.keys():
            if module.moduleName == desc:
                return module
        raise KeyError("Module description `{}` was not found".format(desc))

    @staticmethod
    def makegraph(modules):
        ''' creates a graph based on the given module list '''
        modules = {module.moduleName:module for module in modules}
        g = Graph()
        for module in modules.values():
            g.adj[module]  # dummy invoke to initialize adj for module if not already done
            for desc in module.moduleUses:
                g.addedge(module, modules.get(desc))
        return g
