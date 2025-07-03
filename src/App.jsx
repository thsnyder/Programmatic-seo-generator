import { useState } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { Input } from '@/components/ui/input.jsx'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table.jsx'
import { Textarea } from '@/components/ui/textarea.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { CopyButton } from '@/components/ui/copy-button.jsx'
import { Modal } from '@/components/ui/modal.jsx'
import { MarkdownPreview } from '@/components/ui/markdown-preview.jsx'
import { Plus, FileText, Wand2, Loader2, Sparkles, Eye } from 'lucide-react'
import './App.css'

function App() {
  const [rows, setRows] = useState([
    { id: 1, keyword: '', product: '', contentBrief: '', articleTitle: '', fullArticle: '', metaTitle: '', metaDescription: '', status: 'empty' }
  ])
  const [loadingStates, setLoadingStates] = useState({})
  const [previewModal, setPreviewModal] = useState({ isOpen: false, content: '', title: '' })

  const addRow = () => {
    const newRow = {
      id: Date.now(),
      keyword: '',
      product: '',
      contentBrief: '',
      articleTitle: '',
      fullArticle: '',
      metaTitle: '',
      metaDescription: '',
      status: 'empty'
    }
    setRows([...rows, newRow])
  }

  const updateKeyword = (id, keyword) => {
    setRows(rows.map(row => 
      row.id === id ? { ...row, keyword, status: keyword ? 'keyword-added' : 'empty' } : row
    ))
  }

  const updateProduct = (id, product) => {
    setRows(rows.map(row => 
      row.id === id ? { ...row, product } : row
    ))
  }

  const generateBriefAndTitle = async (id) => {
    const row = rows.find(r => r.id === id)
    if (!row.keyword) return

    setLoadingStates(prev => ({ ...prev, [`brief-${id}`]: true }))
    
    try {
      const response = await fetch('/api/generate_brief_title', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          keyword: row.keyword,
          product: row.product || 'Files.com'
        })
      })
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      const data = await response.json()
      
      setRows(rows.map(r => 
        r.id === id ? { 
          ...r, 
          contentBrief: data.content_brief, 
          articleTitle: data.article_title,
          status: 'brief-generated'
        } : r
      ))
    } catch (error) {
      console.error('Error generating brief:', error)
      alert('Error generating content brief. Please make sure the backend server is running.')
    } finally {
      setLoadingStates(prev => ({ ...prev, [`brief-${id}`]: false }))
    }
  }

  const generateArticle = async (id) => {
    const row = rows.find(r => r.id === id)
    if (!row.contentBrief || !row.articleTitle) return

    setLoadingStates(prev => ({ ...prev, [`article-${id}`]: true }))
    
    try {
      const response = await fetch('/api/generate_article', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          keyword: row.keyword,
          product: row.product || 'Files.com',
          article_title: row.articleTitle,
          content_brief: row.contentBrief
        })
      })
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      const data = await response.json()
      
      setRows(rows.map(r => 
        r.id === id ? { 
          ...r, 
          fullArticle: data.full_article,
          metaTitle: data.meta_title,
          metaDescription: data.meta_description,
          status: 'article-generated'
        } : r
      ))
    } catch (error) {
      console.error('Error generating article:', error)
      alert('Error generating article. Please make sure the backend server is running.')
    } finally {
      setLoadingStates(prev => ({ ...prev, [`article-${id}`]: false }))
    }
  }

  const getStatusBadge = (status) => {
    const statusConfig = {
      'empty': { 
        label: 'Empty', 
        className: 'bg-files-light-gray text-files-headline-black/60 border-files-light-pink' 
      },
      'keyword-added': { 
        label: 'Keyword Added', 
        className: 'bg-files-light-pink text-files-primary-red border-files-super-light-red' 
      },
      'brief-generated': { 
        label: 'Brief Generated', 
        className: 'bg-files-light-pink/60 text-files-maroon border-files-super-light-red' 
      },
      'article-generated': { 
        label: 'Complete', 
        className: 'bg-files-super-light-red/30 text-files-super-dark-maroon border-files-bright-red' 
      }
    }
    
    const config = statusConfig[status] || statusConfig['empty']
    return <Badge className={config.className}>{config.label}</Badge>
  }

  const openPreview = (content, title) => {
    setPreviewModal({ isOpen: true, content, title })
  }

  const closePreview = () => {
    setPreviewModal({ isOpen: false, content: '', title: '' })
  }

  const copyPreviewContent = () => {
    navigator.clipboard.writeText(previewModal.content)
      .then(() => {
        // You could add a toast notification here if desired
        console.log('Article content copied to clipboard')
      })
      .catch(err => {
        console.error('Failed to copy content: ', err)
      })
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-files-light-gray via-files-light-pink to-files-super-light-red p-8">
      <div className="max-w-7xl mx-auto space-y-8">
        {/* Header */}
        <div className="text-center space-y-4">
          <div className="flex items-center justify-center gap-3">
            <div className="p-3 bg-gradient-to-r from-files-primary-red to-files-bright-red rounded-xl shadow-lg">
              <Sparkles className="h-8 w-8 text-white" />
            </div>
            <h1 className="text-4xl font-bold bg-gradient-to-r from-files-primary-red to-files-bright-red bg-clip-text text-transparent">
              SEO Content Generator
            </h1>
          </div>
          <p className="text-lg text-files-headline-black/70 max-w-2xl mx-auto leading-relaxed">
            Transform keywords into comprehensive content briefs and complete articles. 
            Streamline your content creation workflow with AI-powered generation.
          </p>
        </div>

        {/* Main Content */}
        <Card className="shadow-xl border-0 bg-white/90 backdrop-blur-sm">
          <CardHeader className="border-b border-files-light-pink bg-gradient-to-r from-files-light-gray to-files-light-pink/30">
            <div className="flex flex-row items-center justify-between">
              <div>
                <CardTitle className="text-2xl font-semibold text-files-headline-black flex items-center gap-2">
                  <FileText className="h-6 w-6 text-files-primary-red" />
                  Content Pipeline
                </CardTitle>
                <p className="text-files-headline-black/70 mt-1">Manage and generate content across multiple keywords</p>
              </div>
              <Button 
                onClick={addRow} 
                className="bg-gradient-to-r from-files-primary-red to-files-bright-red hover:from-files-maroon hover:to-files-primary-red text-white shadow-lg hover:shadow-xl transition-all duration-200 flex items-center gap-2 px-6 py-3"
              >
                <Plus className="h-5 w-5" />
                Add Row
              </Button>
            </div>
          </CardHeader>
          <CardContent className="p-0">
            <div className="overflow-x-auto">
              <Table>
                <TableHeader>
                  <TableRow className="bg-files-light-pink/30 hover:bg-files-light-pink/30">
                    <TableHead className="w-[180px] text-files-headline-black font-semibold">Keyword</TableHead>
                    <TableHead className="w-[150px] text-files-headline-black font-semibold">Product</TableHead>
                    <TableHead className="w-[220px] text-files-headline-black font-semibold">Content Brief</TableHead>
                    <TableHead className="w-[200px] text-files-headline-black font-semibold">Article Title</TableHead>
                    <TableHead className="w-[280px] text-files-headline-black font-semibold">Full Article</TableHead>
                    <TableHead className="w-[180px] text-files-headline-black font-semibold">Meta Title</TableHead>
                    <TableHead className="w-[220px] text-files-headline-black font-semibold">Meta Description</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {rows.map((row) => (
                    <TableRow key={row.id} className="h-36 hover:bg-files-light-pink/20 transition-colors">
                      <TableCell className="p-4">
                        <div className="space-y-2">
                          <Input
                            placeholder="Enter keyword..."
                            value={row.keyword}
                            onChange={(e) => updateKeyword(row.id, e.target.value)}
                            className="w-full border-files-light-pink focus:border-files-primary-red focus:ring-files-primary-red/20 transition-all"
                          />
                          <div className="flex justify-start mt-1">
                            {getStatusBadge(row.status)}
                          </div>
                        </div>
                      </TableCell>
                      <TableCell className="p-4">
                        <Input
                          placeholder="e.g., Files.com, ExaVault..."
                          value={row.product}
                          onChange={(e) => updateProduct(row.id, e.target.value)}
                          className="w-full border-files-light-pink focus:border-files-primary-red focus:ring-files-primary-red/20 transition-all"
                        />
                      </TableCell>
                      <TableCell className="p-4">
                        <div className="space-y-3">
                          <Button
                            onClick={() => generateBriefAndTitle(row.id)}
                            disabled={!row.keyword || loadingStates[`brief-${row.id}`]}
                            size="sm"
                            className="w-full bg-gradient-to-r from-files-primary-red to-files-bright-red hover:from-files-maroon hover:to-files-primary-red text-white shadow-md hover:shadow-lg transition-all duration-200"
                          >
                            {loadingStates[`brief-${row.id}`] ? (
                              <>
                                <Loader2 className="h-4 w-4 mr-2 animate-spin" />
                                Generating...
                              </>
                            ) : (
                              <>
                                <Wand2 className="h-4 w-4 mr-2" />
                                Generate Brief
                              </>
                            )}
                          </Button>
                          <div className="relative">
                            <Textarea
                              placeholder="Content brief will appear here..."
                              value={row.contentBrief}
                              readOnly
                              className="w-full h-24 resize-none text-sm pr-16 border-files-light-pink focus:border-files-primary-red focus:ring-files-primary-red/20 transition-all bg-files-light-gray/50"
                            />
                            {row.contentBrief && (
                              <div className="absolute top-2 right-2">
                                <CopyButton text={row.contentBrief} />
                              </div>
                            )}
                          </div>
                        </div>
                      </TableCell>
                      <TableCell className="p-4">
                        <div className="space-y-3">
                          <div className="h-8 flex items-center justify-center text-xs text-files-headline-black/60 bg-files-light-pink/30 rounded-md">
                            Auto-generated with brief
                          </div>
                          <div className="relative">
                            <Textarea
                              placeholder="Article title will appear here..."
                              value={row.articleTitle}
                              readOnly
                              className="w-full h-24 resize-none text-sm pr-16 border-files-light-pink focus:border-files-primary-red focus:ring-files-primary-red/20 transition-all bg-files-light-gray/50"
                            />
                            {row.articleTitle && (
                              <div className="absolute top-2 right-2">
                                <CopyButton text={row.articleTitle} />
                              </div>
                            )}
                          </div>
                        </div>
                      </TableCell>
                      <TableCell className="p-4">
                        <div className="space-y-3">
                          <Button
                            onClick={() => generateArticle(row.id)}
                            disabled={!row.contentBrief || !row.articleTitle || loadingStates[`article-${row.id}`]}
                            size="sm"
                            className="w-full bg-gradient-to-r from-files-maroon to-files-primary-red hover:from-files-super-dark-maroon hover:to-files-maroon text-white shadow-md hover:shadow-lg transition-all duration-200"
                          >
                            {loadingStates[`article-${row.id}`] ? (
                              <>
                                <Loader2 className="h-4 w-4 mr-2 animate-spin" />
                                Writing...
                              </>
                            ) : (
                              <>
                                <FileText className="h-4 w-4 mr-2" />
                                Write Article
                              </>
                            )}
                          </Button>
                          <div className="relative">
                            <Textarea
                              placeholder="Full article will appear here..."
                              value={row.fullArticle}
                              readOnly
                              className="w-full h-24 resize-none text-sm pr-16 border-files-light-pink focus:border-files-primary-red focus:ring-files-primary-red/20 transition-all bg-files-light-gray/50"
                            />
                            {row.fullArticle && (
                              <div className="absolute top-2 right-2 flex gap-1">
                                <button
                                  onClick={() => openPreview(row.fullArticle, row.articleTitle)}
                                  className="p-1.5 rounded bg-files-light-pink hover:bg-files-super-light-red text-files-primary-red hover:text-files-maroon transition-all duration-200"
                                  title="Preview Article"
                                >
                                  <Eye className="h-3 w-3" />
                                </button>
                                <CopyButton text={row.fullArticle} />
                              </div>
                            )}
                          </div>
                        </div>
                      </TableCell>
                      <TableCell className="p-4">
                        <div className="space-y-3">
                          <div className="h-8 flex items-center justify-center text-xs text-files-headline-black/60 bg-files-light-pink/30 rounded-md">
                            Auto-generated with article
                          </div>
                          <div className="relative">
                            <Textarea
                              placeholder="Meta title will appear here..."
                              value={row.metaTitle}
                              readOnly
                              className="w-full h-24 resize-none text-sm pr-16 border-files-light-pink focus:border-files-primary-red focus:ring-files-primary-red/20 transition-all bg-files-light-gray/50"
                            />
                            {row.metaTitle && (
                              <div className="absolute top-2 right-2">
                                <CopyButton text={row.metaTitle} />
                              </div>
                            )}
                          </div>
                        </div>
                      </TableCell>
                      <TableCell className="p-4">
                        <div className="space-y-3">
                          <div className="h-8 flex items-center justify-center text-xs text-files-headline-black/60 bg-files-light-pink/30 rounded-md">
                            Auto-generated with article
                          </div>
                          <div className="relative">
                            <Textarea
                              placeholder="Meta description will appear here..."
                              value={row.metaDescription}
                              readOnly
                              className="w-full h-24 resize-none text-sm pr-16 border-files-light-pink focus:border-files-primary-red focus:ring-files-primary-red/20 transition-all bg-files-light-gray/50"
                            />
                            {row.metaDescription && (
                              <div className="absolute top-2 right-2">
                                <CopyButton text={row.metaDescription} />
                              </div>
                            )}
                          </div>
                        </div>
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Article Preview Modal */}
      <Modal
        isOpen={previewModal.isOpen}
        onClose={closePreview}
        title={previewModal.title || 'Article Preview'}
        onCopy={copyPreviewContent}
      >
        <MarkdownPreview content={previewModal.content} />
      </Modal>
    </div>
  )
}

export default App 