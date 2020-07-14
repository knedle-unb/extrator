"""Regex core module.

This module contains the Regex class, which have all that is necessary to
extract a single act or all the acts from a DODF.

Usage Example::

    from dodfminer.extract.regex.core import Regex
    Regex.get_act_obj()

"""

from dodfminer.extract.polished.acts.aposentadoria import Retirements
from dodfminer.extract.polished.acts.reversoes import Revertions
from dodfminer.extract.polished.acts.nomeacao import NomeacaoComissionados
from dodfminer.extract.polished.acts.exoneracao import Exoneracao
from dodfminer.extract.polished.acts.abono import AbonoPermanencia
from dodfminer.extract.polished.acts.retificacoes import RetAposentadoria
from dodfminer.extract.polished.acts.substituicao import Substituicao
from dodfminer.extract.polished.acts.cessoes import Cessoes
from dodfminer.extract.polished.acts.\
     sem_efeito_aposentadoria import SemEfeitoAposentadoria


_acts_ids = {"aposentadoria": Retirements, "reversoes": Revertions,
             "nomeacao": NomeacaoComissionados, "exoneracao": Exoneracao,
             "abono": AbonoPermanencia, "retificacoes": RetAposentadoria,
             "substituicao": Substituicao, "cessoes": Cessoes,
             "sem_efeito_aposentadoria": SemEfeitoAposentadoria}
"""_acts_ids: All avaiable acts classes indexed by a given string name."""


class ActsPropsExtractor:
    """Regex main class.

    All interactions with the acts needs to be done through this interface.
    This class handles all the requests to regex searches.

    Note:
        This class is static

    """

    @staticmethod
    def get_act_obj(ato_id, file, backend):
        """Extract a single act type from a single.

        Object format.

        Args:
            ato_id (string): The name of the act to extract.
            file (string): Path of the file.

        Returns:
            An object of the desired act, already with extracted information.

        """
        
        return _acts_ids[ato_id](file, backend)

    @staticmethod
    def get_all_obj(file, backend):
        """Extract all acts types from a single DODF.

        Object format.

        Args:
            file (string): Path of the file.

        Returns:
            An vector of objects of all the acts, already with extracted
            information.

        """
        res = {}
        for key in _acts_ids:
            res[key] = _acts_ids[key](file, backend)

        return res

    @staticmethod
    def get_act_df(ato_id, file, backend):
        """Extract a single act type from a single DODF.

        Dataframe format.

        Args:
            ato_id (string): The name of the act to extract.
            file (string): Path of the file.

        Returns:
            An dataframe with extracted information, for the desired act.

        """
        return _acts_ids[ato_id](file, backend).data_frame

    @staticmethod
    def get_all_df(file, backend):
        """Extract all acts types from a single DODF.

        Dataframe format.

        Args:
            file (string): Path of the file.

        Returns:
            An vector of dataframed with extracted information for all acts.

        """
        res = {}
        for key in _acts_ids:
            res[key] = _acts_ids[key](file, backend).data_frame

        return res
