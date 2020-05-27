import libsbml

from merge_SBML import read_sbml, get_model, get_Id_organism, get_listOfSpecies, get_ListOfReactions

def get_statistics(textfile, filename):
    """ get number of species and reactions of organism

    :param textfile: file where statistics will be written
    :type textfile: str
    :param filename: an SBML file
    :type filename: str
    """
    document = read_sbml(filename)
    model = get_model(document)
    name = model.getName()
    Id = get_Id_organism(model)
    ListOfSpecies = get_listOfSpecies(model)
    ListOfReactions = get_ListOfReactions(model)
    numSpecies = len(ListOfSpecies)
    numReactions = len(ListOfReactions)
    textfile.write(name)
    textfile.write('\n Id: %s' %(Id))
    textfile.write('\n number of species: %s '%(numSpecies))
    textfile.write('\n number of reactions: %s \n \r' %(numReactions))

def create_info(fileList):
    """ write info.txt

    :param fileList: a list of files
    :type fileList: list
    """
    infofile = open('Results/info.txt', 'w+')
    for filename in fileList:
        get_statistics(infofile, filename)
    infofile.close()
