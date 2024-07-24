![Ivy logo](https://raw.githubusercontent.com/csdms/project/main/assets/CSDMS-logo-color-tagline-hor.png)

# FAIR practices for research software

*FAIR* is

* Findable
* Accessible
* Interoperable
* Reproducible

The FAIR principles for Research Software (FAIR4RS) have been officially endorsed by the [Research Data Alliance](https://www.rd-alliance.org/) and have been published at https://doi.org/10.15497/RDA00068.

Why would you want to make your code FAIR?

From the article:

> The ultimate goal of FAIR is to increase the transparency, reproducibility, and reusability of research. For this to happen, software needs to be well-described (by metadata), inspectable, documented and appropriately structured so that it can be executed, replicated, built-upon, combined, reinterpreted, reimplemented, and/or used in different settings. The FAIR4RS Principles aim to guide software creators and owners on how to make their software FAIR. The FAIR4RS Principles are also relevant to the larger ecosystem and various stakeholders that support research software (e.g., repositories and registries).

What steps can you take to make your code FAIR?

### Findable

> Software and its associated metadata should be easy for both humans and machines to find.

Create a persistent identifier,
such as a [digital object identifier](https://www.doi.org/the-identifier/what-is-a-doi/) (DOI) from [Zenodo](https://zenodo.org/),
for each released or published version of your work.

For example:

* Ivy [![DOI](https://zenodo.org/badge/278206679.svg)](https://zenodo.org/badge/latestdoi/278206679)
* BMI [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3955010.svg)](https://doi.org/10.5281/zenodo.3955010) and
* Landlab [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3776837.svg)](https://doi.org/10.5281/zenodo.3776837)

all have DOIs assigned through Zenodo.

### Accessible

> Software and its metadata is retrievable via standardized protocols

Make your software open source,
ensure that it is well documented with descriptive metadata and narrative documentation in durable text formats (e.g., PDF with no special extensions, .odt OpenOffice Document file, Markdown / plaintext),
and make sure that this metadata remains accessible even if the software is not.

This one is easily accomplished as long as you make your source code available on a community-supported scientific registry or repository, or via GitHub and Zenodo.

### Interoperable

> Software interoperates with other software by exchanging data and/or metadata, and/or through interaction via application programming interfaces (APIs), described through standards.

Your software should read, write, and exchange data using domain-relevant open community standards (e.g., netCDF, HDF, domain-specific controlled vocabularies or ontologies, etc.).
Your software should also include qualified references to other digital research objects.

### Reusable

> Software is both usable (can be executed) and reusable (can be understood, modified, built upon, or incorporated into other software).

Software can be executed and understood, modified, built upon, or incorporated into other software---a clear and accessible license (https://choosealicense.com/), detailed provenance metadata, qualified persistent references to other software dependencies, domain-relevant community standards

## Resources

* Five recommendations for FAIR software: https://fair-software.eu
* Barba (2022): [Defining the role of open source software in research reproducibility](https://arxiv.org/abs/2204.12564)
* Lamprecht *et al.* (2020): [Towards FAIR principles for research software](https://doi.org/10.3233/DS-190026)
    * Anna-Lena Lamprecht's 2021 CSDMS webinar: [FAIR & Research Software](https://csdms.colorado.edu/wiki/Presenters-0548)
* Hinson (2019): [Dealing with Software Collapse](https://doi.org/10.1109/MCSE.2019.2900945) (and original [blog post](http://blog.khinsen.net/posts/2017/01/13/sustainable-software-and-reproducible-research-dealing-with-software-collapse/))
* Jackson (2018): [Software Deposit: What to deposit](https://doi.org/10.5281/zenodo.1327325)
* Gil *et al.* (2016): [Toward the Geoscience Paper of the Future: Best practices for documenting and sharing research from data to software to provenance](https://doi.org/10.1002/2015EA000136)
* Wilson *et al.* (2014): [Best practices for scientific computing](https://doi.org/10.1371/journal.pbio.1001745)
* LeVeque *et al.* (2012): [Reproducible research for scientific computing: Tools and strategies for changing the culture](https://www.computer.org/csdl/magazine/cs/2012/04/mcs2012040013/13rRUy3gn1m)

___

[Best Practices in Software Development](./index.md) |
Previous: [Collaborative projects ("Gitiquette")](./collaboration-etiquette.md)
