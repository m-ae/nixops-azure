#!/usr/bin/env ipython

from nixops.resources import ResourceOptions, ResourceDefinition, ResourceEval
from nixops.plugins import Plugin
from nixops.backends import MachineOptions


class AzurePlugin(Plugin):
    @staticmethod
    def nixexprs():
        return [os.path.dirname(os.path.abspath(__file__)) + "/nix"]


class AzureMachineOptions(ResourceOptions):
    storeKeysOnMachine: bool


class AzureDefinition(ResourceDefinition):

    config: MachineOptions

    store_keys_on_machine: bool

    def __init__(self, name: str, config: ResourceEval):
        super().__init__(name, config)
        self.store_keys_on_machine = config.storeKeysOnMachi
