import libsbml
import os

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
  
def get_ListOfReactants(model):
  ListOfReactants = model.getListOfReactants()
  return ListOfReactants

def get_ListOfProducts(model):
<<<<<<< HEAD:codes_sources/merge_SBML.py
  ListOfProducts = model.getListOfProducts()
  return ListOfProducts
=======
    ListOfProducts = model.getListOfProducts()
    return ListOfProducts
>>>>>>> 30710556c14a7fe43cddaf315f33bc6972472d8a:merano/merge_SBML.py

## Step 4 : Modify Id in a model

def shorten_Id(Id):
  IdList = Id.split("_")
  Id = IdList[-1]
  return Id

def set_UnitDefinitionIds(model, ShortIdOrganism):
  ListOfUnitDefinitions = get_ListOfUnitDefinitions(model)
  for unitDefinition in ListOfUnitDefinitions:
    id = unitDefinition.getIdAttribute()
    newId = id+"_"+ShortIdOrganism
    unitDefinition.setIdAttribute(newId)
  return model

def set_CompartmentIds(model, ShortIdOrganism):
  ListOfCompartments = get_ListOfCompartments(model)
  for compartment in ListOfCompartments:
    id = compartment.getIdAttribute()
    newId = id+"_"+ShortIdOrganism
    compartment.setIdAttribute(newId)
  return model

def set_SpeciesIds(model, ShortIdOrganism):
  ListOfSpecies = get_listOfSpecies(model)
  for species in ListOfSpecies:
    id = species.getIdAttribute()
    newId = id+"_"+ShortIdOrganism
    species.setIdAttribute(newId)
  return model

def set_ParameterIds(model, ShortIdOrganism):
  ListOfParameters = get_ListOfParameters(model)
  for parameter in ListOfParameters:
    id = parameter.getIdAttribute()
    newId = id+"_"+ShortIdOrganism
    parameter.setIdAttribute(newId)
  return model

def set_ReactionsIds(model, ShortIdOrganism):
  ListOfReactions = get_ListOfReactions(model)
  for reaction in ListOfReactions:
    id = reaction.getIdAttribute()
    newId = id+"_"+ShortIdOrganism
    reaction.setIdAttribute(newId)
  return model

def modify_Id(model):
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

def get_SBMLdoc_from_folder():
  folder_path = './Samples/SBML_files'
  fileList = []
  for filename in os.listdir(folder_path):
    fileList.append(filename)
  return fileList

def main_sbml(fileList):
  document=SBMLDocument(3,1)
  model = document.createModel("merged_file")
  for filename in fileList:
    file = read_sbml(filename)
    fileModel = get_model(file)
    fileModel = modify_Id(fileModel)
    model.appendFrom(fileModel)
    print(get_Id_organism(fileModel))
  writeSBML(document, "merged_sbml.xml")

main_sbml(get_SBMLdoc_from_folder())