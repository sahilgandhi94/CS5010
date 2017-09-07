

from collections import defaultdict


class Graph:
    ''' graph implementation to denote the hierarchy of the modules and its dependencies '''

    def __init__(self):
        # initialize an empty adjancy matrix
        self.adj = defaultdict(list)
    
    def __repr__(self):
        # return json.dumps(self.adj, indent=4)
        final = ''
        for key, value in self.adj.items():
            final += '{} --> {}\n'.format(key.moduleName, [module.moduleName for module in value])
        return final
        

    def addedge(self, source, destination):
        ''' add an edge, originating from u and ending at v '''
        self.adj[source].append(destination)

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
