Sample Python Code

from stix2 import Indicator


indicator = Indicator(name="Malevolent Moose",
                      pattern="[file:hashes.md5 = 'e8b3cfe2f8fc25a11eb1e665be0c70bc']",
                      pattern_type="stix")
print(indicator.serialize(pretty=True))


threat_actor1 = ThreatActor(name="Malevolent Moose",
                            description="Disgrunted student organization",
                            threat_actor_types="Hacktivist",
                            first_seen="2024-10-19T16:08:44.492807Z",
                            sophistication="Practitoner",
                            primary_motivation="Ideological")
print(threat_actor1.serialize(pretty=True))
#Define the ongoing campaign against the school
campaign1 = Campaign(name="Operation all A's",
                     aliases="Diploma Pharmers",
                    objective="Grade Tampering")
print(campaign1.serialize(pretty=True))
#Publish their detected malware targeting Brightspace
indicator1 = Indicator(name="DimSpace Grade Changer",
                      pattern="[file:hashes.md5 = 'e8b3cfe2f8fc25a11eb1e665be0c70bc']",
                      pattern_type="stix")
print(indicator1.serialize(pretty=True))
#Define the relationship between an ongoing campaign with the DimSpace malware
relationship1 = Relationship(relationship_type='ReleatedCampaign',
                            source_ref=indicator1.id,
                            target_ref=campaign1.id)
print(relationship1.serialize(pretty=True))
#Define the relationship between an ongoing campaign with the Malevolent Moose Threat Actor
relationship2= Relationship(relationship_type='AssociatedThreatActor',
                            source_ref=threat_actor1.id,
                            target_ref=campaign1.id)
print(relationship2.serialize(pretty=True))
#Create a new bundle with the 5 DSOs
bundle = Bundle(indicator1, campaign1,threat_actor1, relationship1, relationship2)
print(bundle.serialize(pretty=True))
