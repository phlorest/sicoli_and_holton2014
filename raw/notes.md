# Notes

The posterior was rebuilt by SJG using the MrBayes commands listed in the supplementary material on MrBayes 3.2.7a x86_64. 


## Data:

> We applied both Bayesian likelihood modeling and a neighbor joining distance method in
> evaluating typological features of DY, using a binary coding schema that indicates the presence
> or absence of phonological and morphological features. Unknown features for a taxon were coded
> with a question mark. Our data matrix consists of 116 characters for 40 taxa: 2 Yeniseian
> languages (Ket-Kott), 37 Na-Dene (Tlingit-Eyak-Athabascan) languages, and the isolate Haida
> included for its potential as an outgroup. The characters we coded for were based on categories
> represented in Joel Sherzer’s An areal-typological study of American Indian languages north of
> Mexico [26], with some expansion to include more contrasts between Yeniseian and Na-Dene.
> Na-Dene character values were first determined from the Sherzer mono- graph, then checked
> against other published and unpublished sources in the Alaska Native Language Archive and
> revised where more current data was available. Yeniseian language character values were
> determined from a published grammar for the extinct Kott [27], and published grammars for Ket
> [27], [28] with the Ket coding checked by a Yeniseian specialist. Uncertainty was coded with a
> question mark. Of the 116 characters, 26 were excluded as uninformative—either all lacking a
> feature or, to a lesser degree, all possessing a feature—leaving 90 informative characters.


## Methods:

| Model                                | Score    | Program  | Comment            |
|--------------------------------------|----------|----------|--------------------|
| Neighbor-Joining                     |          |SplitsTree|                    |
| Neighbor-Net                         |          |SplitsTree|                    |
| Delta/Q-Residual                     |          |SplitsTree|                    |
| TR + gamma                           |          | MrBayes  |                    |
| TR + gamma + strict clock            |          |          | best-fitting model |
| TR + gamma + relaxed clock           |          |          |                    |
|                                      |          |          |                    |
|                                      |          |          |                    |



## Analysis:

> We ran the MCMC algorithm for 2,000,000 generations sampling every 500 generations to generate 
> 4,001 trees and used a burn-in of 25% to sample 3,001 trees
