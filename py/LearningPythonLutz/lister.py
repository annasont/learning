class ListInstance:
    """
    Klasa ListInstance obsługuje formatowanie ciągów znaków
    zwracanych z funkcji print() i str()
    """
    def __str__(self):
        return '<Instancja klasy %s, adres %s:\n%s>' % (self.__class__.__name__, id(self), self.__attrnames())
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            for attr in sorted(self.__dict__):
                result += '\tatrybut %s=%s\n' % (attr, self.__dict__[attr])
            return result

class ListTree:
    """
    klasa ListTree służy do zwracania tekstowej reprezentacji instacji
    w postaci drzewa dziedziczenia i atrybutów definiowanych na każdym poziomie
    """
    def __str__(self):
        self.__visited = {}
        return '<Instancja klasy {0}, adres {1},:/n{2}{3}>'.format(
            self.__class__.__name__,
            id(self),
            self.__attrnamesall(self, 0),
            self.__listclasses(self.__class__, 4))

    def __listclasses(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Klasa {1}, adres {2}\n'.format(
                dots,
                aClass.__name__,
                id(aClass))
        else:
            self.__visited[aClass] = True
            genabove = (self.__listclasses(c, indent + 4) for c in aClass.__bases__)
            return '\n{0}<Klasa {1}, adres {2}:\n{3}{4}{5}>\n'.format(
                dots, 
                aClass.__name__,
                id(aClass),
                self.__attrnamesall(aClass, indent),
                ''.join(genabove),
                dots)

    def __attrnamesall(self, obj, indent):
        spaces = ' ' * (indent + 4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr[0:2] == '__' and attr[-2:] == '__':
                result += spaces + '{0}=<>\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result

