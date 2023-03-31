import collections

class Graph:
    def __init__(self):
        self.nodes = {}
        self.list = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = []

    def add_edge(self, node1, node2):
        self.add_node(node1.name)
        self.add_node(node2.name)
        if node2 not in self.nodes[node1.name]:
            self.nodes[node1.name].append(node2)
        if node1 not in self.nodes[node2.name]:
            self.nodes[node2.name].append(node1)

    def get_friends_in_country(self, user, country, depth):
        visited = set()
        queue = [(user, 0)]
        while queue:
            current_user, current_depth = queue.pop(0)
            if current_user in visited or current_depth > depth:
                continue
            visited.add(current_user)
            if current_user.country == country:
                yield current_user
            for friend in self.nodes[current_user.name]:
                queue.append((friend, current_depth + 1))

    def get_all_friends(self, user, depth):
        visited = set()
        queue = [(user, 0)]
        while queue:
            current_user, current_depth = queue.pop(0)
            if current_user in visited or current_depth > depth:
                continue
            visited.add(current_user)
            for friend in self.nodes[current_user]:
                queue.append((friend, current_depth + 1))
        print(visited)

    def get_children(self, name):
        return graph.nodes[name]


class User:
    def __init__(self, name, country):
        self.name = name
        self.country = country


graph = Graph()

# Create some users and add them to the graph
jamie = User('Jamie', 'US')
timur = User('Timur', 'UA')
pablo = User('Pablo', 'ES')
carlos = User('Carlos', 'ES')
julie = User('Julie', 'FR')
ricardo = User('Ricardo', 'MX')
graph.add_edge(jamie, timur)
graph.add_edge(timur, pablo)
graph.add_edge(timur, carlos)
graph.add_edge(timur, julie)
graph.add_edge(jamie, ricardo)
graph.add_edge(ricardo, carlos)
graph.add_edge(jamie, pablo)

# Search for friends of friends in Spain
print("All Friends of Jamie in Spain")
for friend in graph.get_friends_in_country(jamie, 'ES', 2):
    print(friend.name)

# Search for all friends
print("All Friends of Timur irrespective of their country")
for friend in (graph.get_children('Timur')):
    print(friend.name)