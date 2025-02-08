# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ptypes/replica.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14ptypes/replica.proto\x12\x06ptypes\x1a\x1bgoogle/protobuf/empty.proto\"$\n\x14ReplicaCreateRequest\x12\x0c\n\x04size\x18\x01 \x01(\t\"9\n\x15ReplicaCreateResponse\x12 \n\x07replica\x18\x01 \x01(\x0b\x32\x0f.ptypes.Replica\"6\n\x12ReplicaGetResponse\x12 \n\x07replica\x18\x01 \x01(\x0b\x32\x0f.ptypes.Replica\"7\n\x13ReplicaOpenResponse\x12 \n\x07replica\x18\x01 \x01(\x0b\x32\x0f.ptypes.Replica\"8\n\x14ReplicaCloseResponse\x12 \n\x07replica\x18\x01 \x01(\x0b\x32\x0f.ptypes.Replica\"9\n\x15ReplicaReloadResponse\x12 \n\x07replica\x18\x01 \x01(\x0b\x32\x0f.ptypes.Replica\"5\n\x14ReplicaRevertRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63reated\x18\x02 \x01(\t\"9\n\x15ReplicaRevertResponse\x12 \n\x07replica\x18\x01 \x01(\x0b\x32\x0f.ptypes.Replica\"\xb8\x01\n\x16ReplicaSnapshotRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cuser_created\x18\x02 \x01(\x08\x12\x0f\n\x07\x63reated\x18\x03 \x01(\t\x12:\n\x06labels\x18\x04 \x03(\x0b\x32*.ptypes.ReplicaSnapshotRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\";\n\x17ReplicaSnapshotResponse\x12 \n\x07replica\x18\x01 \x01(\x0b\x32\x0f.ptypes.Replica\"$\n\x14ReplicaExpandRequest\x12\x0c\n\x04size\x18\x01 \x01(\x03\"9\n\x15ReplicaExpandResponse\x12 \n\x07replica\x18\x01 \x01(\x0b\x32\x0f.ptypes.Replica\"0\n\x11\x44iskRemoveRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\"6\n\x12\x44iskRemoveResponse\x12 \n\x07replica\x18\x01 \x01(\x0b\x32\x0f.ptypes.Replica\"4\n\x12\x44iskReplaceRequest\x12\x0e\n\x06target\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\"7\n\x13\x44iskReplaceResponse\x12 \n\x07replica\x18\x01 \x01(\x0b\x32\x0f.ptypes.Replica\"(\n\x18\x44iskPrepareRemoveRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"L\n\x19\x44iskPrepareRemoveResponse\x12/\n\noperations\x18\x01 \x03(\x0b\x32\x1b.ptypes.PrepareRemoveAction\"(\n\x18\x44iskMarkAsRemovedRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"=\n\x19\x44iskMarkAsRemovedResponse\x12 \n\x07replica\x18\x01 \x01(\x0b\x32\x0f.ptypes.Replica\"*\n\x14RebuildingSetRequest\x12\x12\n\nrebuilding\x18\x01 \x01(\x08\"9\n\x15RebuildingSetResponse\x12 \n\x07replica\x18\x01 \x01(\x0b\x32\x0f.ptypes.Replica\",\n\x19RevisionCounterSetRequest\x12\x0f\n\x07\x63ounter\x18\x01 \x01(\x03\">\n\x1aRevisionCounterSetResponse\x12 \n\x07replica\x18\x01 \x01(\x0b\x32\x0f.ptypes.Replica\"6\n#UnmapMarkDiskChainRemovedSetRequest\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"H\n$UnmapMarkDiskChainRemovedSetResponse\x12 \n\x07replica\x18\x01 \x01(\x0b\x32\x0f.ptypes.Replica\"+\n\x1aSnapshotMaxCountSetRequest\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"?\n\x1bSnapshotMaxCountSetResponse\x12 \n\x07replica\x18\x01 \x01(\x0b\x32\x0f.ptypes.Replica\")\n\x19SnapshotMaxSizeSetRequest\x12\x0c\n\x04size\x18\x01 \x01(\x03\">\n\x1aSnapshotMaxSizeSetResponse\x12 \n\x07replica\x18\x01 \x01(\x0b\x32\x0f.ptypes.Replica\"\xae\x02\n\x08\x44iskInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06parent\x18\x02 \x01(\t\x12\x30\n\x08\x63hildren\x18\x03 \x03(\x0b\x32\x1e.ptypes.DiskInfo.ChildrenEntry\x12\x0f\n\x07removed\x18\x04 \x01(\x08\x12\x14\n\x0cuser_created\x18\x05 \x01(\x08\x12\x0f\n\x07\x63reated\x18\x06 \x01(\t\x12\x0c\n\x04size\x18\x07 \x01(\t\x12,\n\x06labels\x18\x08 \x03(\x0b\x32\x1c.ptypes.DiskInfo.LabelsEntry\x1a/\n\rChildrenEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x95\x04\n\x07Replica\x12\r\n\x05\x64irty\x18\x01 \x01(\x08\x12\x12\n\nrebuilding\x18\x02 \x01(\x08\x12\x0c\n\x04head\x18\x03 \x01(\t\x12\x0e\n\x06parent\x18\x04 \x01(\t\x12\x0c\n\x04size\x18\x05 \x01(\t\x12\x13\n\x0bsector_size\x18\x06 \x01(\x03\x12\x14\n\x0c\x62\x61\x63king_file\x18\x07 \x01(\t\x12\r\n\x05state\x18\x08 \x01(\t\x12\r\n\x05\x63hain\x18\t \x03(\t\x12)\n\x05\x64isks\x18\n \x03(\x0b\x32\x1a.ptypes.Replica.DisksEntry\x12\x18\n\x10remain_snapshots\x18\x0b \x01(\x05\x12\x18\n\x10revision_counter\x18\x0c \x01(\x03\x12\x18\n\x10last_modify_time\x18\r \x01(\x03\x12\x16\n\x0ehead_file_size\x18\x0e \x01(\x03\x12!\n\x19revision_counter_disabled\x18\x0f \x01(\x08\x12%\n\x1dunmap_mark_disk_chain_removed\x18\x10 \x01(\x08\x12\x1c\n\x14snapshot_count_usage\x18\x11 \x01(\x05\x12\x1b\n\x13snapshot_size_usage\x18\x12 \x01(\x03\x12\x1c\n\x14snapshot_count_total\x18\x13 \x01(\x05\x1a>\n\nDisksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.ptypes.DiskInfo:\x02\x38\x01\"E\n\x13PrepareRemoveAction\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x0e\n\x06target\x18\x03 \x01(\t2\xeb\x0b\n\x0eReplicaService\x12N\n\rReplicaCreate\x12\x1c.ptypes.ReplicaCreateRequest\x1a\x1d.ptypes.ReplicaCreateResponse\"\x00\x12\x41\n\rReplicaDelete\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12\x42\n\nReplicaGet\x12\x16.google.protobuf.Empty\x1a\x1a.ptypes.ReplicaGetResponse\"\x00\x12\x44\n\x0bReplicaOpen\x12\x16.google.protobuf.Empty\x1a\x1b.ptypes.ReplicaOpenResponse\"\x00\x12\x46\n\x0cReplicaClose\x12\x16.google.protobuf.Empty\x1a\x1c.ptypes.ReplicaCloseResponse\"\x00\x12H\n\rReplicaReload\x12\x16.google.protobuf.Empty\x1a\x1d.ptypes.ReplicaReloadResponse\"\x00\x12N\n\rReplicaRevert\x12\x1c.ptypes.ReplicaRevertRequest\x1a\x1d.ptypes.ReplicaRevertResponse\"\x00\x12T\n\x0fReplicaSnapshot\x12\x1e.ptypes.ReplicaSnapshotRequest\x1a\x1f.ptypes.ReplicaSnapshotResponse\"\x00\x12N\n\rReplicaExpand\x12\x1c.ptypes.ReplicaExpandRequest\x1a\x1d.ptypes.ReplicaExpandResponse\"\x00\x12\x45\n\nDiskRemove\x12\x19.ptypes.DiskRemoveRequest\x1a\x1a.ptypes.DiskRemoveResponse\"\x00\x12H\n\x0b\x44iskReplace\x12\x1a.ptypes.DiskReplaceRequest\x1a\x1b.ptypes.DiskReplaceResponse\"\x00\x12Z\n\x11\x44iskPrepareRemove\x12 .ptypes.DiskPrepareRemoveRequest\x1a!.ptypes.DiskPrepareRemoveResponse\"\x00\x12Z\n\x11\x44iskMarkAsRemoved\x12 .ptypes.DiskMarkAsRemovedRequest\x1a!.ptypes.DiskMarkAsRemovedResponse\"\x00\x12N\n\rRebuildingSet\x12\x1c.ptypes.RebuildingSetRequest\x1a\x1d.ptypes.RebuildingSetResponse\"\x00\x12]\n\x12RevisionCounterSet\x12!.ptypes.RevisionCounterSetRequest\x1a\".ptypes.RevisionCounterSetResponse\"\x00\x12{\n\x1cUnmapMarkDiskChainRemovedSet\x12+.ptypes.UnmapMarkDiskChainRemovedSetRequest\x1a,.ptypes.UnmapMarkDiskChainRemovedSetResponse\"\x00\x12`\n\x13SnapshotMaxCountSet\x12\".ptypes.SnapshotMaxCountSetRequest\x1a#.ptypes.SnapshotMaxCountSetResponse\"\x00\x12]\n\x12SnapshotMaxSizeSet\x12!.ptypes.SnapshotMaxSizeSetRequest\x1a\".ptypes.SnapshotMaxSizeSetResponse\"\x00\x42\x33Z1github.com/longhorn/types/pkg/generated/enginerpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ptypes.replica_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/longhorn/types/pkg/generated/enginerpc'
  _REPLICASNAPSHOTREQUEST_LABELSENTRY._options = None
  _REPLICASNAPSHOTREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _DISKINFO_CHILDRENENTRY._options = None
  _DISKINFO_CHILDRENENTRY._serialized_options = b'8\001'
  _DISKINFO_LABELSENTRY._options = None
  _DISKINFO_LABELSENTRY._serialized_options = b'8\001'
  _REPLICA_DISKSENTRY._options = None
  _REPLICA_DISKSENTRY._serialized_options = b'8\001'
  _globals['_REPLICACREATEREQUEST']._serialized_start=61
  _globals['_REPLICACREATEREQUEST']._serialized_end=97
  _globals['_REPLICACREATERESPONSE']._serialized_start=99
  _globals['_REPLICACREATERESPONSE']._serialized_end=156
  _globals['_REPLICAGETRESPONSE']._serialized_start=158
  _globals['_REPLICAGETRESPONSE']._serialized_end=212
  _globals['_REPLICAOPENRESPONSE']._serialized_start=214
  _globals['_REPLICAOPENRESPONSE']._serialized_end=269
  _globals['_REPLICACLOSERESPONSE']._serialized_start=271
  _globals['_REPLICACLOSERESPONSE']._serialized_end=327
  _globals['_REPLICARELOADRESPONSE']._serialized_start=329
  _globals['_REPLICARELOADRESPONSE']._serialized_end=386
  _globals['_REPLICAREVERTREQUEST']._serialized_start=388
  _globals['_REPLICAREVERTREQUEST']._serialized_end=441
  _globals['_REPLICAREVERTRESPONSE']._serialized_start=443
  _globals['_REPLICAREVERTRESPONSE']._serialized_end=500
  _globals['_REPLICASNAPSHOTREQUEST']._serialized_start=503
  _globals['_REPLICASNAPSHOTREQUEST']._serialized_end=687
  _globals['_REPLICASNAPSHOTREQUEST_LABELSENTRY']._serialized_start=642
  _globals['_REPLICASNAPSHOTREQUEST_LABELSENTRY']._serialized_end=687
  _globals['_REPLICASNAPSHOTRESPONSE']._serialized_start=689
  _globals['_REPLICASNAPSHOTRESPONSE']._serialized_end=748
  _globals['_REPLICAEXPANDREQUEST']._serialized_start=750
  _globals['_REPLICAEXPANDREQUEST']._serialized_end=786
  _globals['_REPLICAEXPANDRESPONSE']._serialized_start=788
  _globals['_REPLICAEXPANDRESPONSE']._serialized_end=845
  _globals['_DISKREMOVEREQUEST']._serialized_start=847
  _globals['_DISKREMOVEREQUEST']._serialized_end=895
  _globals['_DISKREMOVERESPONSE']._serialized_start=897
  _globals['_DISKREMOVERESPONSE']._serialized_end=951
  _globals['_DISKREPLACEREQUEST']._serialized_start=953
  _globals['_DISKREPLACEREQUEST']._serialized_end=1005
  _globals['_DISKREPLACERESPONSE']._serialized_start=1007
  _globals['_DISKREPLACERESPONSE']._serialized_end=1062
  _globals['_DISKPREPAREREMOVEREQUEST']._serialized_start=1064
  _globals['_DISKPREPAREREMOVEREQUEST']._serialized_end=1104
  _globals['_DISKPREPAREREMOVERESPONSE']._serialized_start=1106
  _globals['_DISKPREPAREREMOVERESPONSE']._serialized_end=1182
  _globals['_DISKMARKASREMOVEDREQUEST']._serialized_start=1184
  _globals['_DISKMARKASREMOVEDREQUEST']._serialized_end=1224
  _globals['_DISKMARKASREMOVEDRESPONSE']._serialized_start=1226
  _globals['_DISKMARKASREMOVEDRESPONSE']._serialized_end=1287
  _globals['_REBUILDINGSETREQUEST']._serialized_start=1289
  _globals['_REBUILDINGSETREQUEST']._serialized_end=1331
  _globals['_REBUILDINGSETRESPONSE']._serialized_start=1333
  _globals['_REBUILDINGSETRESPONSE']._serialized_end=1390
  _globals['_REVISIONCOUNTERSETREQUEST']._serialized_start=1392
  _globals['_REVISIONCOUNTERSETREQUEST']._serialized_end=1436
  _globals['_REVISIONCOUNTERSETRESPONSE']._serialized_start=1438
  _globals['_REVISIONCOUNTERSETRESPONSE']._serialized_end=1500
  _globals['_UNMAPMARKDISKCHAINREMOVEDSETREQUEST']._serialized_start=1502
  _globals['_UNMAPMARKDISKCHAINREMOVEDSETREQUEST']._serialized_end=1556
  _globals['_UNMAPMARKDISKCHAINREMOVEDSETRESPONSE']._serialized_start=1558
  _globals['_UNMAPMARKDISKCHAINREMOVEDSETRESPONSE']._serialized_end=1630
  _globals['_SNAPSHOTMAXCOUNTSETREQUEST']._serialized_start=1632
  _globals['_SNAPSHOTMAXCOUNTSETREQUEST']._serialized_end=1675
  _globals['_SNAPSHOTMAXCOUNTSETRESPONSE']._serialized_start=1677
  _globals['_SNAPSHOTMAXCOUNTSETRESPONSE']._serialized_end=1740
  _globals['_SNAPSHOTMAXSIZESETREQUEST']._serialized_start=1742
  _globals['_SNAPSHOTMAXSIZESETREQUEST']._serialized_end=1783
  _globals['_SNAPSHOTMAXSIZESETRESPONSE']._serialized_start=1785
  _globals['_SNAPSHOTMAXSIZESETRESPONSE']._serialized_end=1847
  _globals['_DISKINFO']._serialized_start=1850
  _globals['_DISKINFO']._serialized_end=2152
  _globals['_DISKINFO_CHILDRENENTRY']._serialized_start=2058
  _globals['_DISKINFO_CHILDRENENTRY']._serialized_end=2105
  _globals['_DISKINFO_LABELSENTRY']._serialized_start=642
  _globals['_DISKINFO_LABELSENTRY']._serialized_end=687
  _globals['_REPLICA']._serialized_start=2155
  _globals['_REPLICA']._serialized_end=2688
  _globals['_REPLICA_DISKSENTRY']._serialized_start=2626
  _globals['_REPLICA_DISKSENTRY']._serialized_end=2688
  _globals['_PREPAREREMOVEACTION']._serialized_start=2690
  _globals['_PREPAREREMOVEACTION']._serialized_end=2759
  _globals['_REPLICASERVICE']._serialized_start=2762
  _globals['_REPLICASERVICE']._serialized_end=4277
# @@protoc_insertion_point(module_scope)
