"""
The MIT License (MIT)

Copyright (c) 2015-2021 Rapptz
Copyright (c) 2022-present tag-epic

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from typing import List, Literal, Optional, TypedDict

from typing_extensions import NotRequired

from .activity import PartialPresenceUpdate
from .channel import GuildChannel
from .emoji import Emoji
from .member import Member
from .role import Role
from .scheduled_events import ScheduledEvent
from .snowflake import Snowflake
from .threads import Thread
from .user import User
from .voice import GuildVoiceState
from .welcome_screen import WelcomeScreen


class Ban(TypedDict):
    reason: Optional[str]
    user: User


class UnavailableGuild(TypedDict):
    id: Snowflake
    unavailable: NotRequired[bool]


DefaultMessageNotificationLevel = Literal[0, 1]
ExplicitContentFilterLevel = Literal[0, 1, 2]
MFALevel = Literal[0, 1]
VerificationLevel = Literal[0, 1, 2, 3, 4]
NSFWLevel = Literal[0, 1, 2, 3]
PremiumTier = Literal[0, 1, 2, 3]
GuildFeature = Literal[
    "AUTO_MODERATION",
    "ANIMATED_ICON",
    "BANNER",
    "COMMUNITY",
    "DISCOVERABLE",
    "FEATURABLE",
    "INVITE_SPLASH",
    "MEMBER_VERIFICATION_GATE_ENABLED",
    "MONETIZATION_ENABLED",
    "MORE_EMOJI",
    "MORE_STICKERS",
    "NEWS",
    "PARTNERED",
    "PREVIEW_ENABLED",
    "PRIVATE_THREADS",
    "SEVEN_DAY_THREAD_ARCHIVE",
    "THREE_DAY_THREAD_ARCHIVE",
    "TICKETED_EVENTS_ENABLED",
    "VANITY_URL",
    "VERIFIED",
    "VIP_REGIONS",
    "WELCOME_SCREEN_ENABLED",
]


class _BaseGuildPreview(UnavailableGuild):
    name: str
    icon: Optional[str]
    splash: Optional[str]
    discovery_splash: Optional[str]
    emojis: List[Emoji]
    features: List[GuildFeature]
    description: Optional[str]


class _GuildPreviewUnique(TypedDict):
    approximate_member_count: int
    approximate_presence_count: int


class GuildPreview(_BaseGuildPreview, _GuildPreviewUnique):
    ...


class Guild(_BaseGuildPreview):
    owner_id: Snowflake
    region: str
    afk_channel_id: Optional[Snowflake]
    afk_timeout: int
    verification_level: VerificationLevel
    default_message_notifications: DefaultMessageNotificationLevel
    explicit_content_filter: ExplicitContentFilterLevel
    roles: List[Role]
    mfa_level: MFALevel
    nsfw_level: NSFWLevel
    application_id: Optional[Snowflake]
    system_channel_id: Optional[Snowflake]
    system_channel_flags: int
    rules_channel_id: Optional[Snowflake]
    vanity_url_code: Optional[str]
    banner: Optional[str]
    premium_tier: PremiumTier
    preferred_locale: str
    public_updates_channel_id: Optional[Snowflake]
    guild_scheduled_events: Optional[List[ScheduledEvent]]
    icon_hash: NotRequired[Optional[str]]
    owner: NotRequired[bool]
    permissions: NotRequired[str]
    widget_enabled: NotRequired[bool]
    widget_channel_id: NotRequired[Optional[Snowflake]]
    joined_at: NotRequired[Optional[str]]
    large: NotRequired[bool]
    member_count: NotRequired[int]
    voice_states: NotRequired[List[GuildVoiceState]]
    members: NotRequired[List[Member]]
    channels: NotRequired[List[GuildChannel]]
    presences: NotRequired[List[PartialPresenceUpdate]]
    threads: NotRequired[List[Thread]]
    max_presences: NotRequired[Optional[int]]
    max_members: NotRequired[int]
    premium_subscription_count: NotRequired[int]
    max_video_channel_users: NotRequired[int]


class InviteGuild(Guild, total=False):
    welcome_screen: WelcomeScreen


class GuildWithCounts(Guild, _GuildPreviewUnique):
    ...


class GuildPrune(TypedDict):
    pruned: Optional[int]


class ChannelPositionUpdate(TypedDict):
    id: Snowflake
    position: Optional[int]
    lock_permissions: Optional[bool]
    parent_id: Optional[Snowflake]


class RolePositionUpdate(TypedDict):
    id: Snowflake
    position: NotRequired[Optional[Snowflake]]
