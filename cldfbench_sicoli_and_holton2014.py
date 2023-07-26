import pathlib

import phlorest


def fix_newick(text):
    return text.replace('prob(percent)', 'prob_percent')


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "sicoli_and_holton2014"

    def cmd_makecldf(self, args):
        self.init(args)

        args.writer.add_summary(
            self.raw_dir.read_tree(
                'phylogeny_deneyeniseian_24April2016.tre',
                preprocessor=fix_newick, detranslate=True),
            self.metadata,
            args.log)
        
        posterior = self.raw_dir.read_trees(
            'posterior.gz',
            burnin=1000, sample=1000, detranslate=True)
        args.writer.add_posterior(posterior, self.metadata, args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus('journal.pone.0091722.s002.NEX'),
            self.characters, 
            args.log)
