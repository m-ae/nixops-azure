#!/usr/bin/env ipython

import nixops.plugins
import nixops.resources
from nixops.plugins import Plugin
from nixops.backends import MachineOptions


class AzurePlugin(Plugin):
    @staticmethod
    def nixexprs():
        return [os.path.dirname(os.path.abspath(__file__)) + "/nix"]


class AzureMachineOptions(nixops.resources.ResourceOptions):
    storeKeysOnMachine: bool


class AzureDefinition(nixops.resources.ResourceDefinition):

    config: MachineOptions

    store_keys_on_machine: bool

    def __init__(self, name: str, config: nixops.resources.ResourceEval):
        super().__init__(name, config)
        self.store_keys_on_machine = config.storeKeysOnMachi
