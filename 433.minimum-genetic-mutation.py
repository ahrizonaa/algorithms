#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        nucleotides = ['A','C','G','T']
        
        def mutations(gene):
            mutations = []
            gene_arr = list(gene)
            for i,base in enumerate(gene_arr):
                for nucleotide in nucleotides:
                    if base == nucleotide:
                        continue
                    mutation = ''.join(gene_arr[0:i]+[nucleotide]+gene_arr[i+1:])
                    if mutation in bank:
                        mutations.append(mutation)
            return mutations
        
        q = deque([(startGene,0)])
        seen = set([startGene])
        while q:
            gene,curr_mutations = q.popleft()
            if gene == endGene:
                return curr_mutations
            
            for mutation in mutations(gene):
                if mutation == endGene:
                    return curr_mutations + 1
                if mutation not in seen:
                    seen.add(mutation)
                    q.append((mutation,curr_mutations+1))
        return -1
# @lc code=end
