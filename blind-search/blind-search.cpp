#include <iostream>
#include <stdio.h>
#include <list>
#include <string>
#include <iomanip>
using namespace std;

const char separator = ' ';
const int currentWidth = 8;
const int listWidth = 30;
template <typename T>
void printElement(T t, const int &width)
{
    cout << left << setw(width) << setfill(separator) << t << "|";
}
struct Node
{
    string tag = "";
    list<Node *> neighbors;

    static void addNode(list<Node *> &nodes)
    {
        Node *newNode = new Node;
        // cout << "Enter tag for the new node: ";
        cin >> newNode->tag;
        nodes.push_back(newNode);
        // cout << "Node added successfully." << "\n";
    }

    static Node *findByTag(list<Node *> &nodes, string tag)
    {
        for (list<Node *>::iterator node_it = nodes.begin(); node_it != nodes.end(); node_it++)
        {
            if ((*node_it)->tag == tag)
                return (*node_it);
        }
        return NULL;
    }

    static void connectNodes(list<Node *> &nodes)
    {
        string tag1, tag2;
        // cout << "Enter tag of first node: ";
        cin >> tag1;
        // cout << "Enter tag of second node: ";
        cin >> tag2;

        Node *node1 = findByTag(nodes, tag1);
        Node *node2 = findByTag(nodes, tag2);

        // Connect nodes if found
        if (node1 && node2)
        {
            node1->neighbors.push_back(node2);
            node2->neighbors.push_back(node1);
            // cout << "Nodes connected successfully." << "\n";
        }
        else if (node1 == NULL)
        {
            // cout << "Node " << tag1 << " does not exists." << "\n";
        }
        else if (node2 == NULL)
        {
            // cout << "Node " << tag2 << " does not exists." << "\n";
        }
    }

    static void displayNodesWithNeighbors(list<Node *> &nodes)
    {
        // cout << "Nodes:" << "\n";
        for (list<Node *>::iterator node_it = nodes.begin(); node_it != nodes.end(); node_it++)
        {
            cout << "Node tag: " << (*node_it)->tag << "\n";
            cout << "Neighbors: ";
            for (list<Node *>::iterator neighbor_it = (*node_it)->neighbors.begin(); neighbor_it != (*node_it)->neighbors.end(); neighbor_it++)
            {
                cout << (*neighbor_it)->tag << " ";
            }
            cout << "\n";
        }
    }
    static string nodesToString(list<Node *> &nodes)
    {
        string nodes_str = "[ ";
        for (list<Node *>::iterator node_it = nodes.begin(); node_it != nodes.end(); node_it++)
        {
            nodes_str += (*node_it)->tag + ", ";
        }
        nodes_str += "]";
        return nodes_str;
    }
};
struct GeneralSearchTree
{
private:
    bool firstInAmplitude = false;
    bool firstInDepth = false;

    Node *next(list<Node *> &nodes_list)
    {
        Node *res = NULL;
        if (firstInAmplitude)
        {
            res = nodes_list.front();
            nodes_list.pop_front();
        }
        else
        {
            res = nodes_list.back();
            nodes_list.pop_back();
        }

        return res;
    }

    void add(list<Node *> &nodes_list, Node *node)
    {
        nodes_list.push_back(node);
    }

    void expand(Node *current)
    {
        for (list<Node *>::iterator neighbor_it = current->neighbors.begin(); neighbor_it != current->neighbors.end(); neighbor_it++)
        {
            if (Node::findByTag(opened_nodes, (*neighbor_it)->tag) == NULL &&
                Node::findByTag(closed_nodes, (*neighbor_it)->tag) == NULL)
            {
                add(opened_nodes, (*neighbor_it));
            }
        }
    }

public:
    GeneralSearchTree(string algorithm)
    {
        if (algorithm == "BFS")
        {
            firstInAmplitude = true;
        }
        else if (algorithm == "DFS")
        {
            firstInDepth = true;
        }
    }

    list<Node *> opened_nodes;
    list<Node *> closed_nodes;
    list<Node *> search(Node *start, Node *destination)
    {
        add(opened_nodes, start);
        Node *current = NULL;

        cout << "|";
        printElement("=========", currentWidth);
        printElement("==============================", listWidth);
        printElement("==============================", listWidth);
        cout << "\n";
        cout << "|";
        printElement(" Current ", currentWidth);
        printElement(" Opened ", listWidth);
        printElement(" Closed ", listWidth);
        cout << "\n";
        cout << "|";
        printElement("=========", currentWidth);
        printElement("==============================", listWidth);
        printElement("==============================", listWidth);
        cout << "\n";

        cout << "| ";
        printElement("-", currentWidth);
        printElement(Node::nodesToString(opened_nodes), listWidth);
        printElement(Node::nodesToString(closed_nodes), listWidth);
        cout << "\n";

        while (!opened_nodes.empty())
        {
            current = next(opened_nodes);
            if (current == destination)
            {
                add(closed_nodes, current);
                cout << "| ";
                printElement(current->tag, currentWidth);
                printElement(Node::nodesToString(opened_nodes), listWidth);
                printElement(Node::nodesToString(opened_nodes), listWidth);
                cout << "\n";
                cout << "====FOUND====\n";
                return closed_nodes;
            }

            add(closed_nodes, current);
            expand(current);
            cout << "| ";
            printElement(current->tag, currentWidth);
            printElement(Node::nodesToString(opened_nodes), listWidth);
            printElement(Node::nodesToString(opened_nodes), listWidth);
            cout << "\n";
        }

        cout << "| ";
        printElement(current->tag, currentWidth);
        printElement(Node::nodesToString(opened_nodes), listWidth);
        printElement(Node::nodesToString(opened_nodes), listWidth);
        cout << "\n";

        return closed_nodes;
    }

    static void initSearch(list<Node *> &graph, string algorithm)
    {

        string startTag, destTag;
        // cout << "Enter tag of start node: ";
        cin >> startTag;
        // cout << "Enter tag of destination node: ";
        cin >> destTag;

        Node *start = Node::findByTag(graph, startTag);
        Node *dest = Node::findByTag(graph, destTag);
        GeneralSearchTree search = GeneralSearchTree(algorithm);

        if (start && dest)
        {
            search.search(start, dest);
        }
        else if (start == NULL)
        {
            // cout << "Node " << startTag << " does not exists." << "\n";
        }
        else if (dest == NULL)
        {
            // cout << "Node " << destTag << " does not exists." << "\n";
        }
    }
};

int main()
{
    list<Node *> graph;
    char choice;

    do
    {
        // cout << "\nMenu:" << "\n";
        // cout << "1. Add Node" << "\n";
        // cout << "2. Connect Nodes" << "\n";
        // cout << "3. Display Nodes with neighbors" << "\n";
        // cout << "4. Depth First Search" << endl;
        // cout << "5. Breadth First Search" << endl;
        // cout << "6. Exit" << "\n";
        // cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
        case '1':
            Node::addNode(graph);
            break;
        case '2':
            Node::connectNodes(graph);
            break;
        case '3':
            Node::displayNodesWithNeighbors(graph);
            break;
        case '4':
        {
            GeneralSearchTree::initSearch(graph, "DFS");
            break;
        }
        case '5':
        {
            GeneralSearchTree::initSearch(graph, "BFS");
            break;
        }
        default:
            // cout << "Invalid choice. Please try again." << "\n";
            break;
        }
    } while (choice != '6');

    // Clean up allocated memory for nodes
    for (list<Node *>::iterator node_it = graph.begin(); node_it != graph.end(); node_it++)
    {
        delete (*node_it);
    }

    return 0;
}