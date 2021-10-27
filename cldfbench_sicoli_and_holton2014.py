import pathlib

import nexus
import phlorest


def fix_newick(p):
    return nexus.NexusReader.from_string(
        p.read_text(encoding='utf8').replace('prob(percent)', 'prob_percent'))


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "sicoli_and_holton2014"

    def cmd_makecldf(self, args):
        self.init(args)
        with self.nexus_summary() as nex:
            self.add_tree_from_nexus(
                args,
                fix_newick(self.raw_dir / 'phylogeny_deneyeniseian_24April2016.tre'),
                nex,
                'summary',
                detranslate=True,
            )
        posterior = self.sample(
            self.read_gzipped_text(
                self.raw_dir / 'DY-26Dec-strict-Hout-ConsensusNetwork-edited.t.nex.gz'),
            detranslate=True,
            as_nexus=True)

        with self.nexus_posterior() as nex:
            for i, tree in enumerate(posterior.trees.trees, start=1):
                self.add_tree(args, tree, nex, 'posterior-{}'.format(i))

        self.add_data(args, self.raw_dir / 'journal.pone.0091722.s002.NEX')
