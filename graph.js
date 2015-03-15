/**
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
* See the GNU General Public License for more details.
* You should have received a copy of the GNU General Public License
* along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/
/**
 * constructor for graph object
 * @param {[type]}
 * @param {[type]}
 */
function Graph( nodes, edges, type ) {
	this.nodes = nodes;
	this.edges = edges;
	this.nodes.forEach( function( node ) {
		node.adj = [];
		node.visited = 0;
	} );
	// 1 for directed or else undirected
	this.type = typeof type !== 'undefined' ? type : 0;
}
Graph.prototype = {
	constructor: Graph,
	/**
	 * Generates adjacency list from a set of edges
	 * @return {null}
	 */
	generateAdjacency: function() {
		for ( var edge in this.edges ) {
			var link = this.edges[edge];
			this.nodes[link.source].adj.push(link.target);
			if ( this.type === 0 ) {
				this.nodes[link.target].adj.push(link.source);
			}
		}
	},
	/**
	 * Runs bfs over the graph
	 * @param {node} node - node to begin bfs from
	 * @return {null}
	 */
	BFS: function( node ) {

	}
};
