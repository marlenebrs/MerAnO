import libsbml
import sys

### Step 1 : Get document and model

def read_sbml(file):
  """ return model of SBML file.
  
  :param file: name of one file "path/name.xml".
  :type file: str

  :returns: the SBMLDocument in the file.
  :rtype: libsbml.SBMLDocument
  """
  document = libsbml.readSBML(file)
  if document.getNumErrors() > 0:
    print("ERROR : \"", file, '\" is not SBML file')
    document.printErrors()
    sys.exit()
  else:
    return document
      
def get_model(document):
  """ get the model from the SBMLDocument.

  :param document: a sbml document.
  :type document: libsbml.SBMLDocument

  :returns: the model from the SBMLDocument.
  """
  model = document.getModel()
  return model

## Step 2 : Define Id for one organism

def get_Id_organism(model):
  """ get the ID of the organism from the model.

  :param model: the model of an sbml document.

  :returns: ID of the organism.
  :rtype: str
  """
  Id = model.getId()
  return Id

## Step 3 :  Get each object

def get_ListOfFunctionDefinitions(model):
  """ get the component ListOfFunctionDefinitions from the model.

  :param model: the model of an sbml document.

  :returns: component ListOfFunctionDefinition from the model.
  """
  ListOfFunctionDefinitions = model.getListOfFunctionDefinitions()
  return ListOfFunctionDefinitions

def get_ListOfUnitDefinitions(model):
  """ get the component ListOfUnitDefinitions from the model.

  :param model: the model of an sbml document.

  :returns: component ListOfUnitDefinitions from the model.
  """
  return model.getListOfUnitDefinitions()

def get_ListOfCompartments(model):
  """ get the component ListOfCompartments from the model.

  :param model: the model of an sbml document.

  :returns: component ListOfCompartments from the model.
  """
  ListOfCompartments = model.getListOfCompartments()
  return ListOfCompartments

def get_listOfSpecies(model):
  """ get the component ListOfSpecies from the model.

  :param model: the model of an sbml document.

  :returns: component ListOfSpecies from the model.
  """
  ListOfSpecies = model.getListOfSpecies()
  return ListOfSpecies

def get_ListOfParameters(model):
  """ get the component ListOfParameters from the model.

  :param model: the model of an sbml document.

  :returns: component ListOfParameters from the model.
  """
  ListOfParameters = model.getListOfParameters()
  return ListOfParameters

def get_ListOfReactions(model):
  """ get the component ListOfReactions from the model.

  :param model: the model of an sbml document.

  :returns: component ListOfReactions from the model.
  """
  ListOfReactions = model.getListOfReactions()
  return ListOfReactions
  
#def get_ListOfReactants(model):
#    ListOfReactants = model.getListOfReactants()
#    return ListOfReactants

#def get_ListOfProducts(model):
#    ListOfProducts = model.getListOfProducts()
#    return ListOfProducts

## Step 4 : Modify Id in a model

def shorten_Id(Id):
  """ selects the end ID of the ID of the organism to make ID shorter.

  :param Id: Id of the organism.
  :type Id: str

  :returns: the end of the organism's ID.
  :rtype: str
  """
  IdList = Id.split("_")
  Id = IdList[-1]
  return Id

def set_UnitDefinitionIds(model, ShortIdOrganism):
  """ changes the ID of the component UnitDefinition.

  :param model: the model of an sbml document.
  :param ShortIdOrganism: a short Id.
  :type ShortIdOrganism: str

  :returns: the model with new ID of component UnitDefinition.
  """
  ListOfUnitDefinitions = get_ListOfUnitDefinitions(model)
  for unitDefinition in ListOfUnitDefinitions:
    id = unitDefinition.getIdAttribute()
    newId = id+"_"+ShortIdOrganism
    unitDefinition.setIdAttribute(newId)
  return model

def set_CompartmentIds(model, ShortIdOrganism):
  """ changes the ID of the component Compartment.

  :param model: the model of an sbml document.
  :param ShortIdOrganism: a short Id.
  :type ShortIdOrganism: str

  :returns: the model with new ID of component Compartment.
  """
  ListOfCompartments = get_ListOfCompartments(model)
  for compartment in ListOfCompartments:
    id = compartment.getIdAttribute()
    newId = id+"_"+ShortIdOrganism
    compartment.setIdAttribute(newId)
  return model

def set_SpeciesIds(model, ShortIdOrganism):
  """ changes the ID of the component Species.

  :param model: the model of an sbml document.
  :param ShortIdOrganism: a short Id.
  :type ShortIdOrganism: str

  :returns: the model with new ID of component Species.
  """
  ListOfSpecies = get_listOfSpecies(model)
  for species in ListOfSpecies:
    id = species.getIdAttribute()
    newId = id+"_"+ShortIdOrganism
    species.setIdAttribute(newId)
  return model

def set_ParameterIds(model, ShortIdOrganism):
  """ changes the ID of the component Parameter.

  :param model: the model of an sbml document.
  :param ShortIdOrganism: a short Id.
  :type ShortIdOrganism: str

  :returns: the model with new ID of component Parameter.
  """
  ListOfParameters = get_ListOfParameters(model)
  for parameter in ListOfParameters:
    id = parameter.getIdAttribute()
    newId = id+"_"+ShortIdOrganism
    parameter.setIdAttribute(newId)
  return model

def set_ReactionsIds(model, ShortIdOrganism):
  """ changes the ID of the component Reactions.

  :param model: the model of an sbml document.
  :param ShortIdOrganism: a short Id.
  :type ShortIdOrganism: str

  :returns: the model with new ID of component Reactions.
  """
  ListOfReactions = get_ListOfReactions(model)
  for reaction in ListOfReactions:
    id = reaction.getIdAttribute()
    newId = id+"_"+ShortIdOrganism
    reaction.setIdAttribute(newId)
  return model

def modify_Id(model):
  """ modify the IDs af all components in model.

  :param model: the model of an sbml document.

  :returns: the model with new IDs for each component.
  """
  Id = get_Id_organism(model)
  ShortId = shorten_Id(Id)
  model = set_UnitDefinitionIds(model, ShortId)
  model = set_CompartmentIds(model, ShortId)
  model = set_SpeciesIds(model, ShortId)
  model = set_ParameterIds(model, ShortId)
  model = set_ReactionsIds(model, ShortId)
  return model

## Step 5 : Create new SBML to merge all documents

from libsbml import *

def main_sbml(fileList):
  """ create one SBML document with all organisms given by user.

  :param fileList: a list with files
  :type fileList: list
  """
  print("Execution in progress ...")
  
  document=SBMLDocument(3,1)
  model = document.createModel("merged_file")
  for filename in fileList:
    file = read_sbml(filename)
    fileModel = get_model(file)
    fileModel = modify_Id(fileModel)
    model.appendFrom(fileModel)
  writeSBML(document, "Results/merged_sbml.xml")


