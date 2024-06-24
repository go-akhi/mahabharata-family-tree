from pyvis.network import Network
import networkx as nx

G = nx.DiGraph()
G.add_edges_from([("Kuru","Shantanu",{"label":"6 Generations"}),
                  ("Dasa","Satyavati"),
                  ("Prasara","Satyavati",{"color":"red"}),
                  ("Satyavati","Shantanu",{"color":"red"}),
                  ("Shantanu","Ganga",{"color":"red"}),
                  ("Shantanu","Bhishma"),("Ganga","Bhishma"),
                  ("Satyavati","Vichitravirya"),("Shantanu","Vichitravirya"),
                  ("Prasara","Vyasa"),("Satyavati","Vyasa"),
                  ("Vyasa","Shudri",{"color":"red"}),
                  ("Vichitravirya", "Ambika",{"color":"red"}),
                  ("Vichitravirya", "Ambalika",{"color":"red"}),
                  ("Vyasa","Ambika",{"color":"red"}),
                  ("Vyasa","Ambalika",{"color":"red"}),
                  ("Vyasa","Vidura"),("Shudri","Vidura"),
                  ("Vyasa","Dhritarashtra"),("Ambika","Dhritarashtra"),
                  ("Vyasa","Pandu"),("Ambalika","Pandu"),
                  ("Pandu","Madri",{"color":"red"}),("Pandu","Kunti",{"color":"red"}),
                  ("Dhritarashtra","Gandhari",{"color":"red"}),
                  ("Gandhari","Duryodhana and the Kauravas"),("Dhritarashtra","Duryodhana and the Kauravas"),
                  ("Surya","Kunti",{"color":"red"}),
                  ("Dharma","Kunti",{"color":"red"}),
                  ("Vayu","Kunti",{"color":"red"}),
                  ("Indra","Kunti",{"color":"red"}),
                  ("Kunti","Karna"),("Surya","Karna"),
                  ("Kunti","Yudhishthira"),("Dharma","Yudhishthira"),
                  ("Kunti","Bhima"),("Vayu","Bhima"),
                  ("Kunti","Arjuna"),("Indra","Arjun"),
                  ("Madri","Nakul"),("Pandu","Nakul"),
                  ("Madri","Sahdev"),("Pandu","Sahdev"),
                  ("Nakula","Draupadi",{"color":"red"}),
                  ("Sahdev","Draupadi",{"color":"red"}),
                  ("Bhima","Draupadi",{"color":"red"}),
                  ("Yudhishthira","Draupadi",{"color":"red"}),
                  ("Draupadi","Prativindhya"),("Yudhushthira","Prativindhya"),
                  ("Draupadi","Sutasoma"),("Bhima","Sutasoma"),
                  ("Draupadi","Srutakarma"),("Sahadeva","Srutakarma"),
                  ("Draupadi","Satatika"),("Nakula","Satatika"),
                  ("Arjun","Draupadi",{"color":"red"}),
                  ("Arjun","Subhadra",{"color":"red"}),
                  ("Arjun","Ulupi",{"color":"red"}),
                  ("Arjun","Chitrangada",{"color":"red"}),
                  ("Arjuna","Srutakirti"),("Draupadi","Srutakirti"),
                  ("Arjuna","Abhimanyu"),("Subhadra","Abhimanyu"),
                  ("Arjuna","Iravan"),("Ulupi","Iravan"),
                  ("Arjuna","Babhruvahana"),("Chitrangada","Babhruvahana"),
                  ("Abhimanyu","Uttara",{"color":"red"}),
                  ("Abhimanyu","Parikchit"),("Uttara","Parikchit"),
                  ("Parikchit","Iravati",{"color":"red"}),
                  ("Parikchit","Janamejay"),("Iravati","Janamejay")])
females=["Satyavati","Ganga","Ambika","Ambalika","Shudri","Madri","Kunti","Gandhari","Draupadi","Subhadra","Ulupi","Chitrangada","Uttara","Iravati"]
for lady in females:
    G.nodes[lady]["color"]="pink"


nt = Network("800px","1200px")
nt.from_nx(G)
nt.show('nx.html', notebook=False)

