
from graphviz import Digraph
# import os
# os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'
if __name__ == '__main__':
    G = Digraph(comment='minicore')
    G.node('D_ENTITY', shape='rect', style = 'bold')
    G.node('D_ACCOUNT', shape='rect')
    G.node('D_AGREEMENT', shape='rect')

    fkeys1 = [('D_ENTITY', 'D_ACCOUNT', 'FK_ACCT___OWNER', True),
              ('D_ENTITY', 'D_ACCOUNT', 'FK_ACCT___DEPT', False),
              ('D_ENTITY', 'D_ACCOUNT', 'FK_ACCT___CNTR', False),
              ('D_ENTITY', 'D_ACCOUNT', 'FK_ACCT___BRNCH', False),
              ('D_ENTITY', 'D_AGREEMENT', 'FK_GMT___DEPT', False),
              ('D_ENTITY', 'D_AGREEMENT', 'FK_AGMT___CNTR', False),
              ('D_ENTITY', 'D_AGREEMENT', 'FK_AGMT___BRNCH', False),
              ('D_ENTITY', 'D_AGREEMENT', 'FK_D_ENTITY', True)]
    for parent, child, fk, ismajor in fkeys1:
        color = 'red' if ismajor else 'black'
        G.edge(parent, child, label=fk, fontsize='10', color=color)

    G.render('C:\graph\minicore1.gv', view=True)
