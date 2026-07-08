from docutils import nodes
from docutils.parsers.rst.directives.parts import Sectnum as SectnumDirective
from docutils.transforms.parts import SectNum as SectnumTransform

class Sectnum(SectnumDirective):
    '''
    Override the Sectnum directive to call custom Sectnum transform
    '''
    def run(self):
        pending = nodes.pending(SectNumTrans)
        pending.details.update(self.options)
        self.state_machine.document.note_pending(pending)
        return [pending]

class SectNumTrans(SectnumTransform):
    '''
    Override `Sectnum` from docutils

    Do not number the uppermost section title, only subjacent ones.
    '''
    start_depth = 1

    def update_section_numbers(self, node, prefix=(), depth=0, level=0):
        depth += 1
        if prefix:
            sectnum = 1
        else:
            sectnum = self.startvalue
        level += 1
        index_rule = 1
        index_directive = 1
        for child in node:
            if isinstance(child, nodes.section):
                title = child[0]

                if level > self.start_depth:
                    numbers = prefix + (str(sectnum),)
                    text = (self.prefix + '.'.join(numbers) + self.suffix + '\u00a0' * 3)
                    generated = nodes.generated('', text, classes=['sectnum'])
                    title.insert(0, generated)
                    title['auto'] = 1
                else:
                    numbers = prefix

                if depth < self.maxdepth:
                    self.update_section_numbers(child, numbers, depth, level)
                sectnum += 1

def setup(app):
    app.add_directive('sectnum', Sectnum)
    return {
        'parallel_read_safe': True,
    }
