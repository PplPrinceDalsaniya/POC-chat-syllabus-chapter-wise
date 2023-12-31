# Available Chapterlist Arrays

availableSubjects = ['science', 'socialscience']

availableDatabase = [
  {
    "path": './Docs/science_ch_2.pdf',
    "subject": 'science',
    "label": 'Ch-2 : Acids, Bases and Salts',
    "id": 'science_ch_2',
    "desc": "Subject Science. Chapter 2: Acids, Bases, and Salts. Explores the properties, reactions, and applications of acids, bases, and salts. It covers their characteristics, pH scale, neutralization reactions, formation of salts, and practical applications."
  },
  {
    "path": './Docs/science_ch_3.pdf',
    "subject": 'science',
    "label": 'Ch-3 : Metals and Non-metals',
    "id": 'science_ch_3',
    "desc": "Subject Science, Chapter 3: Metals and Non-metals. In Class IX you have learnt about various elements. You have seen that elements can be classified as metals or non-metals on the basis of their properties. Think of some uses of metals and non-metals in your daily life. What properties did you think of while categorising elements as metals or non-metals? How are these properties related to the uses of these elements? Let us look at some of these properties in detail."
  },
  {
    "path": './Docs/science_ch_13.pdf',
    "subject": 'science',
    "label": 'Ch-13 : Our Environment',
    "id": 'science_ch_13',
    "desc": "Subject Science, Chapter 13: Our Environment. We have heard the word 'environment' often being used on the television, in newspapers and by people around us. Our elders tell us that the 'environment' is not what it used to be earlier; others say that we should work in a healthy 'environment'; and global summits involving the developed and developing countries are regularly held to discuss 'environmental' issues. In this chapter, we shall be studying how various components in the environment interact with each other and how we impact the environment"
  },
  {
    "path": './Docs/socialscience_ch_2.pdf',
    "subject": 'socialscience',
    "label": 'Ch-2 : Forest and wildlife resources',
    "id": 'socialscience_ch_2',
    "desc": "Subject SocialScience, Chapter 2 : Forest and wildlife resources. We share this planet with millions of other living beings, starting from micro-organisms and bacteria, lichens to banyan trees, elephants and blue whales. This entire habitat that we live in has immense biodiversity. We humans along with all living organisms form a complex web of ecological system in which we are only a part and very much dependent on this system for our own existence. For example, the plants, animals and micro-organisms re-create the quality of the air we breathe, the water we drink and the soil that produces our food without which we cannot survive. Forests play a key role in the ecological system as these are also the primary producers on which all other living beings depend."
  },
  {
    "path": './Docs/socialscience_ch_3.pdf',
    "subject": 'socialscience',
    "label": 'Ch-3 : Water Resources',
    "id": 'socialscience_ch_3',
    "desc": "Subject SocialScience, Chapter 3 : Water Resources. You already know that three-fourth of the earth's surface is covered with water, but only a small proportion of it accounts for freshwater that can be put to use. This freshwater is mainly obtained from surface run off and ground water that is continually being renewed and recharged through the hydrological cycle. All water moves within the hydrological cycle ensuring that water is a renewable resource."
  },
  {
    "path": './Docs/socialscience_ch_4.pdf',
    "subject": 'socialscience',
    "label": 'Ch-4 : Agriculture',
    "id": 'socialscience_ch_4',
    "desc": "Subject SocialScience, Chapter 4 : Agriculture. India is an agriculturally important country. Two-thirds of its population is engaged in agricultural activities. Agriculture is a primary activity, which produces most of the food that we consume. Besides food grains, it also produces raw material for various industries. This chapter explores the agriculture sector of india."
  },
]


# getAllParams : ex. getAllLabels || getAllIds || etc
def get_all_param(targetParam):
  result = []
  for entry in availableDatabase:
    if targetParam in entry:
      result.append(entry[targetParam])
  return result


# getValueByParams : ex. get label for this id
def get_value_by_param(targetParam, searchParam, searchValue):
  for chapter in availableDatabase:
    if chapter[searchParam] == searchValue:
      return chapter[targetParam]
  return None


# getTargetParamsForThisValues : ex. getDescForThisIds || getDescForThisLabels
def get_target_params_for_this_values(targetParam, searchParam, searchValues):
  result = []
  for chapter in availableDatabase:
    if chapter[searchParam] in searchValues:
      result.append(chapter[targetParam])
  return result
