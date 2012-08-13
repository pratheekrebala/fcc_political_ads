from moderation import moderation
from moderation.moderator import GenericModerator
from locations.models import Address, AddressLabel


class DefaultModerator(GenericModerator):
    auto_approve_for_staff = False

moderation.register(Address, DefaultModerator)
moderation.register(AddressLabel, DefaultModerator)