import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from resources.datatables import FactionStatus
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('cheerleader_rebel_commando_hard')
	mobileTemplate.setLevel(89)
	mobileTemplate.setDifficulty(Difficulty.ELITE)

	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(1)
	mobileTemplate.setSocialGroup("rebel")
	mobileTemplate.setAssistRange(0)
	mobileTemplate.setStalker(True)
	mobileTemplate.setFaction("rebel")
	mobileTemplate.setFactionStatus(FactionStatus.Combatant)
	
	templates = Vector()
	templates.add('object/mobile/shared_dressed_rebel_commando_human_female_01.iff')
	templates.add('object/mobile/shared_dressed_rebel_commando_human_male_01.iff')
	templates.add('object/mobile/shared_dressed_rebel_commando_moncal_male_01.iff')
	templates.add('object/mobile/shared_dressed_rebel_commando_rodian_male_01.iff')
	templates.add('object/mobile/shared_dressed_rebel_commando_twilek_female_01.iff')
	templates.add('object/mobile/shared_dressed_rebel_commando_zabrak_female_01.iff')			
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/ranged/carbine/shared_carbine_e5.iff', WeaponType.CARBINE, 1.0, 15, 'energy')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('rangedShot')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('elite_rebel_commando_89', mobileTemplate)
	return