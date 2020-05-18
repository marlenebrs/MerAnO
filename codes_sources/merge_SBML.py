import libsbml

### Step 1 : Get document and model

def read_sbml(file):
  """
  return model of SBML file 
  """
  document = libsbml.readSBML(file)
  if document.getNumErrors() > 0:
    print("Encountered the following SBML errors:" + "\n")
    document.printErrors()
    else:
      return document
      
def get_model(document):
  model = document.getModel()
  return model

## Step 2 : Define Id for one organism

def get_Id_organism(model):
  Id = model.getId()
  return Id

## Step 3 :  Get each object

def get_ListOfFunctionDefinitions(model):
  ListOfFunctionDefinitions = model.getListOfFunctionDefinitions()
  return ListOfFunctionDefinitions

def get_ListOfUnitDefinitions(model):
  return model.getListOfUnitDefinitions()

def get_ListOfCompartments(model):
    ListOfCompartments = model.getListOfCompartments()
    return ListOfCompartments

def get_listOfSpecies(model):
  ListOfSpecies = model.getListOfSpecies()
  return ListOfSpecies

def get_ListOfParameters(model):
  ListOfParameters = model.getListOfParameters()
  return ListOfParameters

def get_ListOfReactions(model):
    ListOfReactions = model.getListOfReactions()
    return ListOfReactions

## Step 4 : Modify Id in a model

def shorten_Id(Id):
  IdList = Id.split("_")
  Id = IdList[-1]
  return Id

def set_UnitDefinitionIds(ListOfUnitDefinitions, ShortIdOrganism):
  for unitDefinition in ListOfUnitDefinitions:
    id = unitDefinition.getIdAttribute()
    newId = id+"_"+ShortIdOrganism
    unitDefinition.setIdAttribute(newId)
  return ListOfUnitDefinitions

def set_CompartmentIds(ListOfCompartments, ShortIdOrganism):
  for compartment in ListOfCompartments:
    id = compartment.getIdAttribute()
    newId = id+"_"+ShortIdOrganism
    compartment.setIdAttribute(newId)
  return ListOfCompartments

def set_SpeciesIds(ListOfSpecies, ShortIdOrganism):
  for species in ListOfSpecies:
    id = species.getIdAttribute()
    newId = id+"_"+ShortIdOrganism
    species.setIdAttribute(newId)
  return ListOfSpecies

def set_ParameterIds(ListOfParameters, ShortIdOrganism):
  for parameter in ListOfParameters:
    id = parameter.getIdAttribute()
    newId = id+"_"+ShortIdOrganism
    parameter.setIdAttribute(newId)
  return ListOfParameters

def set_ReactionsIds(ListOfReactions, ShortIdOrganism):
  for reaction in ListOfReactions:
    id = reaction.getIdAttribute()
    newId = id+"_"+ShortIdOrganism
    reaction.setIdAttribute(newId)
  return ListOfReactions

# def modify_Id(model):
#   return model

## Step 5 : Create new SBML to merge all documents

from libsbml import *

document=SBMLDocument(3,1)

model=document.createModel("Projet")


def create_Definition():
    definition = model.createDefinition()
    definition = ListOfFunctionDefinitions
    definition = ListOfUnitDefinitions
    return create_Definition

def create_Compartment():
    compartment = model.createCompartment()
    compartment = ListOfCompartments
    return create_Compartment

def create_Species():
    species = model.createSpecies()
    species = ListOfSpecies
    return create_Species

def create_Parameters():
    parameters = model.createParameters()
    parameters = ListOfParameters
    return create_Parameters

def create_Reactions():
    reaction = model.createReaction()
    reaction = ListOfReactions
    return create_Reactions

writeSBML(document,"projet.xml")
